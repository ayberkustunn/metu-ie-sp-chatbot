"""
Retriever module — builds a FAISS vector index over the knowledge base
and performs semantic search with relevance scoring.
"""

import json
import numpy as np
from typing import List, Dict, Tuple
import hashlib
import os

from knowledge_base import KNOWLEDGE_CHUNKS, CURATED_FAQ


def _get_cache_path() -> str:
    return os.path.join(os.path.dirname(__file__), ".embedding_cache.json")


def _load_cache() -> dict:
    path = _get_cache_path()
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}


def _save_cache(cache: dict):
    path = _get_cache_path()
    with open(path, "w") as f:
        json.dump(cache, f)


def _hash_text(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def get_embedding(text: str, client, cache: dict) -> List[float]:
    """Get embedding for a text, using cache if available."""
    key = _hash_text(text)
    if key in cache:
        return cache[key]
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )
    emb = response.data[0].embedding
    cache[key] = emb
    return emb


def build_documents() -> List[Dict]:
    """Combine knowledge chunks and curated FAQ into a flat document list."""
    docs = []
    for chunk in KNOWLEDGE_CHUNKS:
        docs.append(
            {
                "id": chunk["id"],
                "text": chunk["content"],
                "topic": chunk["topic"],
                "source_url": chunk["source_url"],
                "page_title": chunk["page_title"],
            }
        )
    for i, faq in enumerate(CURATED_FAQ):
        docs.append(
            {
                "id": f"faq-curated-{i}",
                "text": f"Q: {faq['question']}\nA: {faq['answer']}",
                "topic": faq["question"],
                "source_url": faq["source_url"],
                "page_title": "Curated FAQ",
            }
        )
    return docs


def build_index(client) -> Tuple[object, List[Dict], np.ndarray]:
    """Build FAISS index over all documents. Returns (index, docs, embeddings)."""
    import faiss

    docs = build_documents()
    cache = _load_cache()

    texts = [d["text"] for d in docs]
    embeddings = [None] * len(texts)
    
    uncached_texts = []
    uncached_indices = []

    for i, t in enumerate(texts):
        key = _hash_text(t)
        if key in cache:
            embeddings[i] = cache[key]
        else:
            uncached_texts.append(t)
            uncached_indices.append(i)

    # Process uncached texts in batches to dramatically speed up initial index building
    if uncached_texts:
        batch_size = 100
        for i in range(0, len(uncached_texts), batch_size):
            batch = uncached_texts[i:i+batch_size]
            response = client.embeddings.create(
                model="text-embedding-3-small",
                input=batch,
            )
            for j, data in enumerate(response.data):
                idx = uncached_indices[i+j]
                emb = data.embedding
                embeddings[idx] = emb
                cache[_hash_text(batch[j])] = emb
        
        _save_cache(cache)

    emb_matrix = np.array(embeddings, dtype="float32")
    # Normalize for cosine similarity
    faiss.normalize_L2(emb_matrix)
    dim = emb_matrix.shape[1]
    index = faiss.IndexFlatIP(dim)  # Inner product on normalized = cosine sim
    index.add(emb_matrix)

    return index, docs, emb_matrix


def search(
    query: str,
    index,
    docs: List[Dict],
    client,
    top_k: int = 5,
    threshold: float = 0.35,
) -> List[Dict]:
    """Search the index for relevant documents. Returns list of matches with scores."""
    import faiss

    cache = _load_cache()
    q_emb = np.array([get_embedding(query, client, cache)], dtype="float32")
    faiss.normalize_L2(q_emb)
    _save_cache(cache)

    scores, indices = index.search(q_emb, top_k)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue
        if score < threshold:
            continue
        doc = docs[idx].copy()
        doc["relevance_score"] = float(score)
        results.append(doc)

    return results


def keyword_fallback(query: str, docs: List[Dict], top_k: int = 3) -> List[Dict]:
    """Simple keyword-based fallback when vector search returns nothing."""
    query_lower = query.lower()
    tokens = set(query_lower.split())
    scored = []
    for doc in docs:
        text_lower = doc["text"].lower()
        topic_lower = doc["topic"].lower()
        hits = sum(1 for t in tokens if t in text_lower or t in topic_lower)
        if hits > 0:
            scored.append((hits, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [s[1] for s in scored[:top_k]]
