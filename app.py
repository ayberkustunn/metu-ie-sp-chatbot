"""
METU IE Summer Practice Assistant
===================================
RAG chatbot for METU IE Summer Practice (IE 300 / IE 400).
Data source: https://sp-ie.metu.edu.tr/en
"""

import streamlit as st
from openai import OpenAI
from retriever import build_index, search, keyword_fallback, build_documents
from prompts import SYSTEM_PROMPT, format_context, format_history, is_out_of_scope

# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="ODTÜ IE Yaz Stajı Asistanı | METU IE Summer Practice",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════════════════════════
# METU LOGO (base64)
# ═══════════════════════════════════════════════════════════════════════════
METU_LOGO = "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"

# ═══════════════════════════════════════════════════════════════════════════
# DARK / LIGHT MODE — persisted via query_params (survives page refresh)
# ═══════════════════════════════════════════════════════════════════════════
_qp = st.query_params
if "dark_mode" not in st.session_state:
    # Restore from URL query param if available, default to dark
    st.session_state.dark_mode = _qp.get("theme", "dark") != "light"

IS_DARK = st.session_state.dark_mode

# ── Base CSS (always applied) ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"], .stMarkdown {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.stDeployButton { display: none; }
div[data-testid="stToolbar"] { display: none; }
div[data-testid="manage-app-button"] { display: none; }
.viewerBadge_container__r5tak { display: none !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 0.5rem !important; }

/* Mobile responsiveness */
@media (max-width: 768px) {
    .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
    .wh h2 { font-size: 1.25rem !important; }
    .wh p { font-size: 0.82rem !important; }
    .lr { width: 52px !important; height: 52px !important; }
    .li { width: 42px !important; height: 42px !important; }
    .li img { width: 32px !important; height: 32px !important; }
}

/* Source pills */
.src-label {
    font-size: 0.67rem; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.1em; opacity: 0.45; margin: 0.6rem 0 0.25rem;
}
.src-pill {
    display: inline-flex; align-items: center; gap: 0.25rem;
    padding: 0.22rem 0.6rem; border-radius: 999px;
    font-size: 0.68rem; font-weight: 600; text-decoration: none !important;
    border: 1px solid rgba(128,128,128,0.25);
    margin: 0.12rem 0.15rem 0.12rem 0; transition: all 0.15s; opacity: 0.7;
}
.src-pill:hover { border-color: #C8102E; color: #C8102E !important; opacity: 1; }

/* Welcome */
.wh { text-align: center; padding: 0.8rem 0 0.3rem; }
.wh h2 { font-size: 1.55rem; font-weight: 800; letter-spacing: -0.02em; margin: 0 0 0.25rem; line-height: 1.25; }
.wh .ac { color: #C8102E; }
.wh p { font-size: 0.92rem; opacity: 0.55; margin: 0; }

/* Logo ring */
.lr {
    width: 64px; height: 64px; border-radius: 50%; margin: 0 auto 0.7rem;
    background: linear-gradient(135deg, #C8102E, #E8384F);
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 3px 12px rgba(200,16,46,0.18);
}
.li {
    width: 52px; height: 52px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center; overflow: hidden;
}
.li img { width: 40px; height: 40px; object-fit: contain; }

/* Footer */
.ft {
    text-align: center; font-size: 0.58rem; text-transform: uppercase;
    letter-spacing: 0.12em; font-weight: 600; opacity: 0.3; padding: 0.4rem 0 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# ── Theme-specific CSS ──
if IS_DARK:
    st.markdown("""
    <style>
    .stApp { background-color: #0f1117 !important; color: #e6e6e9 !important; }
    header[data-testid="stHeader"],
    .stApp > header { background-color: #0f1117 !important; }
    section[data-testid="stSidebar"] { background-color: #16181f !important; }
    section[data-testid="stSidebar"] > div { background-color: #16181f !important; }
    .li { background: #111 !important; }
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li { color: #c8c8cc !important; }
    [data-testid="stSidebar"] .stMarkdown a { color: #7eb4f5 !important; }
    [data-testid="stSidebar"] .stMarkdown strong { color: #e0e0e3 !important; }
    [data-testid="stSidebar"] .stElementContainer label { color: #c8c8cc !important; }
    .brand-title { color: #FF6B82 !important; }
    .brand-sub { color: #9a9aa0 !important; }
    .stChatMessage { background: transparent !important; border: none !important; }
    /* Main area text colors — exclude sidebar */
    .stApp .stMarkdown p,
    .stApp .stMarkdown li,
    .stApp .stMarkdown span { color: #e2e2e6 !important; }
    .stApp .stMarkdown strong { color: #FF6B80 !important; }
    .stApp .stMarkdown a { color: #7eb4f5 !important; }
    /* Re-apply sidebar-specific overrides */
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li { color: #c8c8cc !important; }
    /* Chat input */
    [data-testid="stChatInput"],
    [data-testid="stChatInput"] > div,
    [data-testid="stBottom"],
    [data-testid="stBottom"] > div { background-color: #1a1c24 !important; border-color: #2a2d38 !important; }
    [data-testid="stChatInput"] textarea,
    [data-testid="stBottom"] textarea { color: #e2e2e6 !important; background-color: #1a1c24 !important; }
    [data-testid="stChatInput"] button,
    [data-testid="stBottom"] button { color: #e2e2e6 !important; }
    .src-pill { color: #9ab0cc !important; border-color: rgba(150,170,200,0.25) !important; background: #1a1c24 !important; }
    /* Scope button styling — global then sidebar override */
    .stButton > button { background-color: #1a1c24 !important; color: #c8c8cc !important; border-color: #2a2d38 !important; }
    .stButton > button:hover { background-color: #252830 !important; border-color: #C8102E !important; color: #e6e6e9 !important; }
    [data-testid="stSidebar"] .stButton > button { background-color: #1e2028 !important; }
    [data-testid="stSidebar"] .stButton > button:hover { background-color: #252830 !important; }
    h1, h2, h3, h4, h5 { color: #e6e6e9 !important; }
    .wh h2 { color: #e6e6e9 !important; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp { background-color: #fafafa !important; color: #1a1a2e !important; }
    header[data-testid="stHeader"],
    .stApp > header { background-color: #fafafa !important; }
    section[data-testid="stSidebar"] { background-color: #ffffff !important; }
    section[data-testid="stSidebar"] > div { background-color: #ffffff !important; }
    .li { background: #ffffff !important; }
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li { color: #4a4a5a !important; }
    [data-testid="stSidebar"] .stMarkdown a { color: #1a5fb4 !important; }
    [data-testid="stSidebar"] .stMarkdown strong { color: #1a1a2e !important; }
    [data-testid="stSidebar"] .stElementContainer label { color: #4a4a5a !important; }
    .brand-title { color: #C8102E !important; }
    .brand-sub { color: #888 !important; }
    .stChatMessage { background: transparent !important; border: none !important; }
    /* Main area text colors — exclude sidebar */
    .stApp .stMarkdown p,
    .stApp .stMarkdown li,
    .stApp .stMarkdown span { color: #2a2a3e !important; }
    .stApp .stMarkdown strong { color: #C8102E !important; }
    .stApp .stMarkdown a { color: #1a5fb4 !important; }
    /* Re-apply sidebar-specific overrides */
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li { color: #4a4a5a !important; }
    /* Chat input */
    [data-testid="stChatInput"],
    [data-testid="stChatInput"] > div,
    [data-testid="stBottom"],
    [data-testid="stBottom"] > div { background-color: #ffffff !important; border-color: #e0e0e8 !important; }
    [data-testid="stChatInput"] textarea,
    [data-testid="stBottom"] textarea { color: #1a1a2e !important; background-color: #ffffff !important; }
    [data-testid="stChatInput"] button,
    [data-testid="stBottom"] button { color: #1a1a2e !important; }
    .src-pill { color: #4a5f78 !important; border-color: rgba(0,0,0,0.1) !important; background: #f0f0f5 !important; }
    /* Scope button styling — global then sidebar override */
    .stButton > button { background-color: #ffffff !important; color: #2a2a3e !important; border-color: #e0e0e8 !important; }
    .stButton > button:hover { background-color: #f5f5fa !important; border-color: #C8102E !important; color: #1a1a2e !important; }
    [data-testid="stSidebar"] .stButton > button { background-color: #f0f0f5 !important; }
    [data-testid="stSidebar"] .stButton > button:hover { background-color: #e8e8ed !important; }
    h1, h2, h3, h4, h5 { color: #1a1a2e !important; }
    .wh h2 { color: #1a1a2e !important; }
    </style>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════
with st.sidebar:
    # ── Branding ──
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:0.55rem;padding:0.2rem 0 0.3rem;">'
        f'<img src="data:image/png;base64,{METU_LOGO}" width="30" height="30"'
        f' style="border-radius:6px;background:#111;padding:2px;"/>'
        f'<div>'
        f'<div class="brand-title" style="font-size:0.88rem;font-weight:800;line-height:1.15;">'
        f'IE Summer Practice<br>Assistant</div>'
        f'<div class="brand-sub" style="font-size:0.5rem;text-transform:uppercase;letter-spacing:0.1em;'
        f'font-weight:700;">METU Industrial Engineering</div>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

    # ── Theme toggle ──
    dark_on = st.toggle(
        "🌙 Dark mode",
        value=st.session_state.dark_mode,
        key="dark_toggle",
    )
    if dark_on != st.session_state.dark_mode:
        st.session_state.dark_mode = dark_on
        st.query_params["theme"] = "dark" if dark_on else "light"
        st.rerun()

    st.divider()

    # ── Quick Links ──
    st.markdown("**🔗 Quick Links**")
    st.markdown(
        "- [SP Website (Main Page)](https://sp-ie.metu.edu.tr/en)\n"
        "- [General Information](https://sp-ie.metu.edu.tr/en/general-information)\n"
        "- [Steps to Follow](https://sp-ie.metu.edu.tr/en/steps-follow)\n"
        "- [FAQ](https://sp-ie.metu.edu.tr/en/faq)\n"
        "- [SP Committee](https://sp-ie.metu.edu.tr/en/sp-committee)"
    )
    st.caption("📄 Documents, Forms & SP Opportunities are available on the SP Website main page.")

    st.divider()

    # ── IE Curriculum Links (NEW) ──
    st.markdown("**📚 IE Curriculum**")
    st.markdown(
        "- [Prerequisite Chain](https://ie.metu.edu.tr/en/prerequisite-chain)\n"
        "- [IE Curriculum (EN)](https://ie.metu.edu.tr/en/bs-industrial-engineering-curriculum)\n"
        "- [IE Müfredatı (TR)](https://ie.metu.edu.tr/tr/endustri-muhendisligi-lisans-ogretim-programi)"
    )

    st.divider()

    # ── Sample Questions ──
    st.markdown("**💬 Try asking**")
    st.caption("• How do I apply for SGK insurance?")
    st.caption("• What are the requirements for IE 300?")
    st.caption("• Can I do my internship abroad?")
    st.caption("• What are the prerequisites for IE 300?")
    st.caption("• Who do I contact for SP questions?")

    st.divider()

    # ── Clear Chat ──
    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    # ── Contact ──
    st.markdown("**📬 Contact**")
    st.caption("📧 ie-staj@metu.edu.tr")
    st.caption("📠 +90 (312) 210 4786")
    st.caption("🏢 Office: IE 129")


# ═══════════════════════════════════════════════════════════════════════════
# BACKEND INITIALIZATION — UNTOUCHED
# ═══════════════════════════════════════════════════════════════════════════
@st.cache_resource
def get_client():
    api_key = st.secrets.get("OPENAI_API_KEY", "")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)

@st.cache_resource
def get_index(_client):
    idx, docs, _ = build_index(_client)
    return idx, docs

client = get_client()
if client is None:
    st.error(
        "⚠️ **OpenAI API key not found.**\n\n"
        "If you are the app administrator, add `OPENAI_API_KEY` to Streamlit Cloud Secrets.\n\n"
        "If you are a student, please contact the project team — the service may be temporarily unavailable."
    )
    st.stop()

with st.spinner("Loading knowledge base..."):
    index, docs = get_index(client)

if "messages" not in st.session_state:
    st.session_state.messages = []


# ═══════════════════════════════════════════════════════════════════════════
# PREFILL — must be popped BEFORE welcome screen renders
# ═══════════════════════════════════════════════════════════════════════════
_prefill = st.session_state.pop("_prefill", None)


# ═══════════════════════════════════════════════════════════════════════════
# WELCOME SCREEN — only when no messages AND no pending prefill
# ═══════════════════════════════════════════════════════════════════════════
if not st.session_state.messages and not _prefill:
    st.markdown(
        f'<div class="wh">'
        f'<div class="lr"><div class="li">'
        f'<img src="data:image/png;base64,{METU_LOGO}" alt="METU"/>'
        f'</div></div>'
        f"<h2>Merhaba! Ben <span class='ac'>IE Yaz Stajı Asistanınızım</span></h2>"
        f'<p>IE 300 &amp; IE 400 Yaz Stajları hakkında size nasıl yardımcı olabilirim?</p>'
        f'<p style="font-size:0.8rem;opacity:0.4;margin-top:0.3rem;">Ask me anything about IE 300 &amp; IE 400 Summer Practice</p>'
        f'</div>',
        unsafe_allow_html=True,
    )
    st.write("")

    # Suggestion buttons — click to ask the assistant
    st.caption("💡 Aşağıdaki konulardan birini seçin veya kendi sorunuzu yazın:")
    suggestions = [
        ("📋 IE 300 Gereksinimleri", "IE 300 için gereksinimler nelerdir?"),
        ("🏥 SGK Başvurusu", "SGK sigortası için nasıl başvuru yapabilirim?"),
        ("📄 Belgeler ve Formlar", "Staj için hangi belge ve formları teslim etmem gerekiyor?"),
        ("🌍 Yurt Dışı Staj", "Yurt dışında staj yapabilir miyim?"),
    ]
    c1, c2 = st.columns(2)
    for i, (label, query) in enumerate(suggestions):
        with (c1 if i % 2 == 0 else c2):
            if st.button(label, key=f"sug_{i}", use_container_width=True):
                st.session_state["_prefill"] = query
                st.rerun()


# ═══════════════════════════════════════════════════════════════════════════
# CHAT HISTORY — UNTOUCHED
# ═══════════════════════════════════════════════════════════════════════════
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and msg.get("sources"):
            st.markdown(msg["sources"], unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
# CHAT INPUT — CRITICAL FIX: always render st.chat_input() first,
# then check prefill separately. Never short-circuit with `or`.
# ═══════════════════════════════════════════════════════════════════════════
typed_input = st.chat_input("IE 300, IE 400, SGK, staj raporu hakkında sorun... / Ask about summer practice...")
user_input = _prefill if _prefill else typed_input

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # ── Out-of-scope check (UNTOUCHED) ──
    if is_out_of_scope(user_input):
        oos = (
            "Üzgünüm, ancak ben yalnızca ODTÜ Endüstri Mühendisliği Yaz Stajları "
            "(IE 300 ve IE 400) hakkında yardımcı olmak üzere tasarlanmış bir asistanım. "
            "Bu konuda bilgi veremiyorum.\n\n"
            "*I'm sorry, but I'm designed only to assist with METU IE Summer Practice "
            "(IE 300 and IE 400) questions.*\n\n"
            "Staj süreçleriyle ilgili bir sorunuz varsa memnuniyetle yanıtlarım! 🎓"
        )
        st.session_state.messages.append({"role": "assistant", "content": oos, "sources": ""})
        with st.chat_message("assistant"):
            st.markdown(oos)
        st.stop()

    # ── Retrieval (UNTOUCHED) ──
    with st.spinner("Searching knowledge base..."):
        results = search(user_input, index, docs, client, top_k=5, threshold=0.35)
        if not results:
            results = keyword_fallback(user_input, docs, top_k=3)

    context = format_context(results)
    history = format_history(st.session_state.messages[:-1])
    system_msg = SYSTEM_PROMPT.format(context=context, history=history)

    # ── Generation ──
    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.1,
                max_tokens=800,
                stream=True,
            )
            answer = st.write_stream(
                (chunk.choices[0].delta.content or "")
                for chunk in stream
                if chunk.choices[0].delta.content is not None
            )
        except Exception as e:
            import traceback
            traceback.print_exc()
            answer = (
                "I'm sorry, I encountered an error while processing your question. "
                "Please try again in a moment, or visit the official SP website at "
                "**sp-ie.metu.edu.tr** or contact **ie-staj@metu.edu.tr** for assistance."
            )
            st.markdown(answer)

        # ── Sources (same logic) ──
        sources_html = ""
        if results:
            seen = set()
            pills = []
            for r in results:
                url = r["source_url"].rstrip(".,;:!? ")  # FIX #6: strip trailing punctuation
                if url not in seen:
                    seen.add(url)
                    pills.append(
                        f'<a href="{url}" target="_blank" rel="noopener noreferrer" class="src-pill">'
                        f'🔗 {r["page_title"]}</a>'
                    )
            sources_html = f'<div class="src-label">Sources</div>{"".join(pills)}'
            st.markdown(sources_html, unsafe_allow_html=True)

    st.session_state.messages.append({
        "role": "assistant", "content": answer, "sources": sources_html,
    })

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════
st.markdown(
    '<div class="ft">IE Summer Practice Assistant · Data from sp-ie.metu.edu.tr · '
    'AI-generated content may require verification</div>',
    unsafe_allow_html=True,
)
