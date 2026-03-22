"""
METU IE Summer Practice Assistant
===================================
A RAG-based chatbot for METU IE Summer Practice (IE 300 / IE 400).
Design: "Academic Architect" — inspired by Linear + ChatGPT aesthetics.
Data: https://sp-ie.metu.edu.tr/en
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
    page_title="IE Summer Practice Assistant",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── Design System CSS ────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

/* ═══ ROOT VARIABLES ═══ */
:root {
    --metu-red: #C8102E;
    --coral: #FF4D6A;
    --surface-dark: #111318;
    --surface-dark-1: #1a1b21;
    --surface-dark-2: #282a2f;
    --surface-dark-3: #33353a;
    --text-dark-primary: #e2e2e9;
    --text-dark-secondary: #abc9f2;
    --outline-dark: rgba(90, 64, 65, 0.15);
    --green-accent: #5bde90;
}

/* ═══ GLOBAL OVERRIDES ═══ */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* ═══ MAIN CONTAINER ═══ */
.stApp > header { display: none; }
section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

/* ═══ SIDEBAR STYLING ═══ */
section[data-testid="stSidebar"] {
    background-color: #f7f8fa;
    border-right: none !important;
    box-shadow: 2px 0 20px rgba(0,0,0,0.04);
}
@media (prefers-color-scheme: dark) {
    section[data-testid="stSidebar"] {
        background-color: #1a1b21 !important;
        box-shadow: 2px 0 24px rgba(0,0,0,0.3);
    }
}
[data-theme="dark"] section[data-testid="stSidebar"],
.stApp[data-theme="dark"] section[data-testid="stSidebar"] {
    background-color: #1a1b21 !important;
}

/* ═══ SIDEBAR LINK STYLING ═══ */
.sidebar-link {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    padding: 0.6rem 0.85rem;
    border-radius: 10px;
    color: #4a5f78;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    transition: all 0.2s ease;
    margin-bottom: 2px;
}
.sidebar-link:hover {
    background: rgba(200, 16, 46, 0.06);
    color: #C8102E;
    text-decoration: none;
}
.sidebar-link-icon {
    font-size: 1.1rem;
    opacity: 0.7;
    width: 20px;
    text-align: center;
}

/* ═══ WELCOME HERO ═══ */
.welcome-hero {
    text-align: center;
    padding: 2rem 1rem 1rem 1rem;
}
.welcome-hero h1 {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    margin-bottom: 0.4rem;
    line-height: 1.2;
}
.welcome-hero h1 .accent {
    color: #C8102E;
}
.welcome-hero .subtitle {
    font-size: 1.05rem;
    color: #6b7280;
    font-weight: 500;
    margin-bottom: 2rem;
}

/* ═══ QUICK START CARDS ═══ */
.qs-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
    max-width: 600px;
    margin: 0 auto 2rem auto;
}
.qs-card {
    background: #f7f8fa;
    border: 1px solid transparent;
    border-radius: 14px;
    padding: 1.1rem 1.2rem;
    cursor: pointer;
    transition: all 0.25s ease;
    text-align: left;
}
.qs-card:hover {
    background: #fff;
    border-color: rgba(200,16,46,0.12);
    box-shadow: 0 8px 24px rgba(200,16,46,0.06);
    transform: translateY(-1px);
}
.qs-card-icon {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: rgba(200,16,46,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    margin-bottom: 0.6rem;
    color: #C8102E;
}
.qs-card h3 {
    font-size: 0.85rem;
    font-weight: 700;
    margin: 0 0 0.25rem 0;
    color: #1a1b21;
}
.qs-card p {
    font-size: 0.75rem;
    color: #6b7280;
    margin: 0;
    line-height: 1.45;
}

/* ═══ DARK MODE CARDS ═══ */
@media (prefers-color-scheme: dark) {
    .qs-card {
        background: #1a1b21;
        border-color: rgba(90,64,65,0.15);
    }
    .qs-card:hover {
        background: #282a2f;
        border-color: rgba(255,77,106,0.2);
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    .qs-card-icon { background: rgba(255,77,106,0.12); color: #FF4D6A; }
    .qs-card h3 { color: #e2e2e9; }
    .qs-card p { color: #abc9f2; opacity: 0.6; }
    .welcome-hero h1 .accent { color: #FF4D6A; }
    .welcome-hero .subtitle { color: #abc9f2; opacity: 0.7; }
    .sidebar-link { color: #abc9f2; opacity: 0.7; }
    .sidebar-link:hover { background: rgba(255,77,106,0.08); color: #FF4D6A; opacity: 1; }
}

/* ═══ CHAT MESSAGES ═══ */
[data-testid="stChatMessage"] {
    border: none !important;
    background: transparent !important;
    padding: 0.5rem 0 !important;
}

/* User message bubble */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) > div:last-child {
    background: linear-gradient(135deg, #FF4D6A 0%, #C8102E 100%) !important;
    color: #fff !important;
    border-radius: 22px 22px 6px 22px !important;
    padding: 0.85rem 1.25rem !important;
    box-shadow: 0 4px 16px rgba(200,16,46,0.2);
    max-width: 85%;
    margin-left: auto;
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) > div:last-child p {
    color: #fff !important;
}

/* Bot message bubble */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) > div:last-child {
    background: #f7f8fa !important;
    border: 1px solid rgba(0,0,0,0.05) !important;
    border-radius: 6px 22px 22px 22px !important;
    padding: 1.1rem 1.4rem !important;
    max-width: 90%;
}
@media (prefers-color-scheme: dark) {
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) > div:last-child {
        background: #1a1b21 !important;
        border-color: rgba(90,64,65,0.15) !important;
    }
}

/* ═══ SOURCE PILLS ═══ */
.source-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 600;
    text-decoration: none;
    margin: 0.2rem 0.2rem 0.2rem 0;
    transition: all 0.2s ease;
    background: #f0f0f5;
    color: #4a5f78;
    border: 1px solid rgba(0,0,0,0.06);
}
.source-pill:hover {
    border-color: rgba(200,16,46,0.25);
    color: #C8102E;
    text-decoration: none;
}
@media (prefers-color-scheme: dark) {
    .source-pill {
        background: #282a2f;
        color: #abc9f2;
        border-color: rgba(90,64,65,0.2);
    }
    .source-pill:hover {
        border-color: rgba(255,77,106,0.3);
        color: #FF4D6A;
    }
}
.sources-label {
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #9ca3af;
    margin-top: 0.8rem;
    margin-bottom: 0.4rem;
}

/* ═══ CHAT INPUT ═══ */
[data-testid="stChatInput"] {
    border-radius: 999px !important;
    border-color: rgba(0,0,0,0.08) !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: rgba(200,16,46,0.3) !important;
    box-shadow: 0 0 0 3px rgba(200,16,46,0.08) !important;
}

/* ═══ FOOTER ═══ */
.app-footer {
    text-align: center;
    font-size: 0.62rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    font-weight: 600;
    color: #9ca3af;
    padding: 0.5rem 0 1rem 0;
    opacity: 0.6;
}

/* ═══ LOGO CIRCLE ═══ */
.logo-ring {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: linear-gradient(135deg, #C8102E 0%, #FF4D6A 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.2rem auto;
    box-shadow: 0 8px 32px rgba(200,16,46,0.2);
}
.logo-inner {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    font-weight: 900;
    color: #C8102E;
}
@media (prefers-color-scheme: dark) {
    .logo-inner { background: #1a1b21; color: #FF4D6A; }
}

/* ═══ HIDE STREAMLIT DEFAULTS ═══ */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.stDeployButton { display: none; }
div[data-testid="stToolbar"] { display: none; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="margin-bottom: 0.5rem;">
        <div style="font-size: 1.15rem; font-weight: 800; color: #C8102E; line-height: 1.25;">
            IE Summer Practice<br>Assistant
        </div>
        <div style="font-size: 0.6rem; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; opacity: 0.45; margin-top: 0.25rem;">
            Academic Architect v1.0
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <a href="https://sp-ie.metu.edu.tr/en" target="_blank" class="sidebar-link">
        <span class="sidebar-link-icon">🌐</span> SP Website
    </a>
    <a href="https://sp-ie.metu.edu.tr/en/general-information" target="_blank" class="sidebar-link">
        <span class="sidebar-link-icon">ℹ️</span> General Info
    </a>
    <a href="https://sp-ie.metu.edu.tr/en/steps-follow" target="_blank" class="sidebar-link">
        <span class="sidebar-link-icon">📋</span> Steps to Follow
    </a>
    <a href="https://sp-ie.metu.edu.tr/en/forms" target="_blank" class="sidebar-link">
        <span class="sidebar-link-icon">📄</span> Documents & Forms
    </a>
    <a href="https://sp-ie.metu.edu.tr/en/faq" target="_blank" class="sidebar-link">
        <span class="sidebar-link-icon">❓</span> FAQ
    </a>
    <a href="https://sp-ie.metu.edu.tr/en/sp-committee" target="_blank" class="sidebar-link">
        <span class="sidebar-link-icon">👥</span> SP Committee
    </a>
    <a href="https://sp-ie.metu.edu.tr/en/sp-opportunities" target="_blank" class="sidebar-link">
        <span class="sidebar-link-icon">💼</span> SP Opportunities
    </a>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="font-size: 0.72rem; color: #9ca3af; line-height: 1.5; padding: 0.3rem 0;">
        📧 <strong>Contact:</strong> ie-staj@metu.edu.tr<br>
        📠 <strong>Fax:</strong> +90 (312) 210 4786<br>
        🏢 <strong>Office:</strong> IE 129
    </div>
    """, unsafe_allow_html=True)


# ── Initialize OpenAI Client ────────────────────────────────────────────
@st.cache_resource
def get_client():
    api_key = st.secrets.get("OPENAI_API_KEY", "")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


@st.cache_resource
def get_index(_client):
    index, docs, _ = build_index(_client)
    return index, docs


client = get_client()

if client is None:
    st.error("⚠️ OpenAI API key not found. Add `OPENAI_API_KEY` to Streamlit secrets.")
    st.stop()

with st.spinner("Loading knowledge base..."):
    index, docs = get_index(client)


# ── Chat State ───────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []


# ── Welcome Screen (shown when no messages yet) ─────────────────────────
if not st.session_state.messages:
    st.markdown("""
    <div class="welcome-hero">
        <div class="logo-ring">
            <div class="logo-inner">IE</div>
        </div>
        <h1>Hi, I'm the <span class="accent">IE Summer Practice Assistant.</span></h1>
        <p class="subtitle">Ask me anything about IE 300 & IE 400 Summer Practice.</p>
    </div>
    """, unsafe_allow_html=True)

    # Quick start cards
    st.markdown("""
    <div class="qs-grid">
        <div class="qs-card" onclick="
            document.querySelector('[data-testid=stChatInput] textarea').value='What are the requirements for IE 300?';
            document.querySelector('[data-testid=stChatInput] textarea').dispatchEvent(new Event('input', {bubbles:true}));
        ">
            <div class="qs-card-icon">📋</div>
            <h3>IE 300 Requirements</h3>
            <p>Guidelines for the first mandatory summer practice.</p>
        </div>
        <div class="qs-card" onclick="
            document.querySelector('[data-testid=stChatInput] textarea').value='How do I apply for SGK insurance?';
            document.querySelector('[data-testid=stChatInput] textarea').dispatchEvent(new Event('input', {bubbles:true}));
        ">
            <div class="qs-card-icon">🏥</div>
            <h3>SGK Insurance</h3>
            <p>Step-by-step insurance application process via OCW.</p>
        </div>
        <div class="qs-card" onclick="
            document.querySelector('[data-testid=stChatInput] textarea').value='What documents and forms do I need?';
            document.querySelector('[data-testid=stChatInput] textarea').dispatchEvent(new Event('input', {bubbles:true}));
        ">
            <div class="qs-card-icon">📄</div>
            <h3>Documents & Forms</h3>
            <p>Application forms, manuals, and evaluation templates.</p>
        </div>
        <div class="qs-card" onclick="
            document.querySelector('[data-testid=stChatInput] textarea').value='Can I do my internship abroad?';
            document.querySelector('[data-testid=stChatInput] textarea').dispatchEvent(new Event('input', {bubbles:true}));
        ">
            <div class="qs-card-icon">🌍</div>
            <h3>Internship Abroad</h3>
            <p>Erasmus, international placements, and requirements.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Display Chat History ─────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and "sources" in msg:
            st.markdown(
                f'<div class="sources-label">Sources</div>{msg["sources"]}',
                unsafe_allow_html=True,
            )

# ── Chat Input ───────────────────────────────────────────────────────────
if user_input := st.chat_input("Ask about IE 300, IE 400, SGK, reports, deadlines..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Out-of-scope check
    if is_out_of_scope(user_input):
        oos_response = (
            "That's outside what I can help with! I'm here for **METU IE Summer Practice** questions — "
            "feel free to ask me anything about IE 300, IE 400, SGK insurance, reports, finding companies, etc. 🎓"
        )
        st.session_state.messages.append({"role": "assistant", "content": oos_response})
        with st.chat_message("assistant"):
            st.markdown(oos_response)
        st.stop()

    # Retrieval
    with st.spinner("Searching knowledge base..."):
        results = search(user_input, index, docs, client, top_k=5, threshold=0.35)
        if not results:
            results = keyword_fallback(user_input, docs, top_k=3)

    context = format_context(results)
    history = format_history(st.session_state.messages[:-1])
    system_msg = SYSTEM_PROMPT.format(context=context, history=history)

    # Generation
    with st.chat_message("assistant"):
        with st.spinner(""):
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

        # Source pills
        sources_html = ""
        if results:
            seen = set()
            pills = []
            for r in results:
                key = r["source_url"]
                if key not in seen:
                    seen.add(key)
                    pills.append(
                        f'<a href="{r["source_url"]}" target="_blank" class="source-pill">'
                        f'🔗 {r["page_title"]}</a>'
                    )
            sources_html = "".join(pills)
            st.markdown(
                f'<div class="sources-label">Sources</div>{sources_html}',
                unsafe_allow_html=True,
            )

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources_html,
    })

# ── Footer ───────────────────────────────────────────────────────────────
st.markdown(
    '<div class="app-footer">IE Summer Practice Assistant · Data from sp-ie.metu.edu.tr · AI-generated content may require verification</div>',
    unsafe_allow_html=True,
)
