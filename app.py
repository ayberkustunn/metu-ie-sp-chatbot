"""
METU IE Summer Practice Chatbot
================================
A RAG-based chatbot that answers questions about METU Industrial Engineering
Summer Practices (IE 300 / IE 400) using content from https://sp-ie.metu.edu.tr/en

Deployment: Streamlit Cloud
Authors: IE 304 Project Group
"""

import streamlit as st
from openai import OpenAI

from retriever import build_index, search, keyword_fallback, build_documents
from prompts import (
    SYSTEM_PROMPT,
    format_context,
    format_history,
    is_out_of_scope,
)

# ── Page Config ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="METU IE Summer Practice Chatbot",
    page_icon="🎓",
    layout="centered",
)

# ── Custom CSS ───────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }
    .main-header h1 {
        font-size: 1.8rem;
        margin-bottom: 0.2rem;
    }
    .main-header p {
        color: #666;
        font-size: 0.95rem;
    }
    .source-link {
        font-size: 0.82rem;
        color: #888;
        margin-top: 0.3rem;
    }
    .disclaimer {
        font-size: 0.78rem;
        color: #999;
        text-align: center;
        padding: 0.5rem;
        border-top: 1px solid #eee;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Header ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="main-header">
        <h1>🎓 METU IE Summer Practice Assistant</h1>
        <p>Ask me anything about IE 300 & IE 400 Summer Practices</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Sidebar ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### About")
    st.markdown(
        "This chatbot answers questions about **METU Industrial Engineering "
        "Summer Practice** (IE 300 / IE 400) based on the "
        "[official SP website](https://sp-ie.metu.edu.tr/en)."
    )
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown(
        "- [SP Website](https://sp-ie.metu.edu.tr/en)\n"
        "- [General Info](https://sp-ie.metu.edu.tr/en/general-information)\n"
        "- [Steps to Follow](https://sp-ie.metu.edu.tr/en/steps-follow)\n"
        "- [Documents/Forms](https://sp-ie.metu.edu.tr/en/forms)\n"
        "- [FAQ](https://sp-ie.metu.edu.tr/en/faq)\n"
        "- [SP Committee](https://sp-ie.metu.edu.tr/en/sp-committee)"
    )
    st.markdown("---")
    st.markdown("### Sample Questions")
    st.markdown(
        "- How do I apply for SGK insurance?\n"
        "- What are the requirements for IE 300?\n"
        "- Can I do my SP abroad?\n"
        "- What forms do I need to submit?\n"
        "- How long should the internship be?"
    )
    st.markdown("---")
    st.markdown(
        '<p class="disclaimer">Built for IE 304 Project 1<br>'
        "Data source: sp-ie.metu.edu.tr</p>",
        unsafe_allow_html=True,
    )


# ── Initialize OpenAI Client ────────────────────────────────────────────
@st.cache_resource
def get_client():
    api_key = st.secrets.get("OPENAI_API_KEY", "")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


@st.cache_resource
def get_index(_client):
    """Build FAISS index (cached so it only runs once)."""
    index, docs, _ = build_index(_client)
    return index, docs


client = get_client()

if client is None:
    st.error(
        "⚠️ OpenAI API key not found. Please add `OPENAI_API_KEY` to "
        "`.streamlit/secrets.toml` or Streamlit Cloud secrets."
    )
    st.stop()

# Build index
with st.spinner("Loading knowledge base..."):
    index, docs = get_index(client)

# ── Chat State ───────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Chat Input ───────────────────────────────────────────────────────────
if user_input := st.chat_input("Ask about METU IE Summer Practice..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # ── Out-of-scope check ───────────────────────────────────────────
    if is_out_of_scope(user_input):
        oos_response = (
            "This question is outside my scope. I can only help with "
            "**METU IE Summer Practice (IE 300 / IE 400)** related topics.\n\n"
            "For other queries, please contact your academic advisor or visit "
            "[METU IE Department](https://ie.metu.edu.tr)."
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": oos_response}
        )
        with st.chat_message("assistant"):
            st.markdown(oos_response)
        st.stop()

    # ── Retrieval ────────────────────────────────────────────────────
    with st.spinner("Searching knowledge base..."):
        results = search(user_input, index, docs, client, top_k=5, threshold=0.35)
        if not results:
            results = keyword_fallback(user_input, docs, top_k=3)

    context = format_context(results)
    history = format_history(st.session_state.messages[:-1])  # Exclude current

    # ── Generation ───────────────────────────────────────────────────
    system_msg = SYSTEM_PROMPT.format(context=context, history=history)

    with st.chat_message("assistant"):
        with st.spinner("Generating answer..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.1,
                max_tokens=800,
            )
            answer = response.choices[0].message.content

        st.markdown(answer)

        # Show sources
        if results:
            sources = set()
            for r in results:
                sources.add(f"[{r['page_title']}]({r['source_url']})")
            source_text = " · ".join(sources)
            st.markdown(
                f'<p class="source-link">📎 Sources: {source_text}</p>',
                unsafe_allow_html=True,
            )

    st.session_state.messages.append({"role": "assistant", "content": answer})
