import os
import json
import glob
import subprocess
from pypdf import PdfReader

INTERNSHIP_DIR = "/Users/ayberkustun/Desktop/İNTERNSHİ"
OUTPUT_FILE = "/Users/ayberkustun/Desktop/projeson/document_chunks.json"

def extract_text_from_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Failed to read PDF {filepath}: {e}")
        return ""

def extract_text_from_doc(filepath):
    try:
        # Uses MacOS textutil to convert .doc and .docx to raw text
        result = subprocess.run(
            ["textutil", "-convert", "txt", filepath, "-stdout"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except Exception as e:
        print(f"Failed to read DOC/DOCX {filepath}: {e}")
        return ""

def chunk_text(text, filename, chunk_size=1000, overlap=200):
    text = text.replace('\n', ' ').strip()
    words = text.split(' ')
    chunks = []
    
    current_chunk = []
    current_len = 0
    
    for word in words:
        if current_len + len(word) > chunk_size and len(current_chunk) > 0:
            chunks.append(" ".join(current_chunk))
            # keep overlapping words
            overlap_words = current_chunk[-overlap//5:] if len(current_chunk) > overlap//5 else current_chunk
            current_chunk = overlap_words
            current_len = sum(len(w) for w in current_chunk) + len(current_chunk)
            
        current_chunk.append(word)
        current_len += len(word) + 1
        
    if current_chunk:
        chunks.append(" ".join(current_chunk))
        
    docs = []
    for i, c in enumerate(chunks):
        if len(c.strip()) > 50: # filter out tiny useless chunks
            docs.append({
                "id": f"doc-{filename}-{i}",
                "topic": f"Document: {filename}",
                "source_url": f"local_file://{filename}",
                "page_title": filename,
                "content": c.strip()
            })
    return docs

def main():
    all_chunks = []
    
    # Process PDFs
    pdf_files = glob.glob(os.path.join(INTERNSHIP_DIR, "*.pdf"))
    for pdf_file in pdf_files:
        filename = os.path.basename(pdf_file)
        print(f"Processing {filename}...")
        text = extract_text_from_pdf(pdf_file)
        if text:
            # specifically for PDFs which often have huge text, we want larger chunks
            chunks = chunk_text(text, filename, chunk_size=1200, overlap=200)
            all_chunks.extend(chunks)

    # Process DOC and DOCX
    doc_files = glob.glob(os.path.join(INTERNSHIP_DIR, "*.doc*"))
    for doc_file in doc_files:
        filename = os.path.basename(doc_file)
        print(f"Processing {filename}...")
        text = extract_text_from_doc(doc_file)
        if text:
            chunks = chunk_text(text, filename, chunk_size=1000, overlap=150)
            all_chunks.extend(chunks)

    print(f"Total chunks extracted: {len(all_chunks)}")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=4, ensure_ascii=False)
    print(f"Successfully saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
