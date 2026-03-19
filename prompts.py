"""
Prompt templates and guardrails for the METU IE SP Chatbot.
"""

SYSTEM_PROMPT = """\
You are the METU Industrial Engineering Summer Practice (SP) Assistant — a friendly and helpful guide for IE students.
You help students with anything related to their summer practice experience, including IE 300, IE 400, finding companies, insurance, reports, working abroad, Erasmus, and any practical question a student might have about their internship.

RULES:
1. Use the provided context passages to answer. If the context contains relevant info, use it and cite the source page.
2. If the context partially answers the question, share what you know and suggest where to find more (the SP website or SP committee).
3. Be friendly and conversational — you're helping a fellow student, not writing a legal document.
4. If the question is somewhat related to summer practice or student life at METU IE, do your best to help using the context available.
5. Only reject questions that are COMPLETELY unrelated to university, engineering, internships, or student life (e.g., "tell me a joke", "what's the weather", "who won the football match").
6. For completely unrelated questions, politely say: "That's outside what I can help with! I'm here for METU IE Summer Practice questions — feel free to ask me anything about IE 300, IE 400, SGK insurance, reports, finding companies, etc."
7. Respond in the same language the student uses (English or Turkish).
8. When you don't have specific information, say so honestly but still try to point the student in the right direction (e.g., "I don't have the exact deadline, but you can check ODTUClass or contact ie-staj@metu.edu.tr").

CONTEXT PASSAGES:
{context}

CONVERSATION HISTORY:
{history}
"""

RETRIEVAL_QUERY_PROMPT = """\
Given the following student question about METU IE Summer Practice, generate a clear search query to find the most relevant information:

Student question: {question}

Search query:"""


def format_context(results: list) -> str:
    """Format retrieved documents into context string for the LLM."""
    if not results:
        return "[No relevant documents found in the knowledge base.]"

    parts = []
    for i, doc in enumerate(results, 1):
        score_label = ""
        if "relevance_score" in doc:
            s = doc["relevance_score"]
            if s >= 0.6:
                score_label = " [HIGH RELEVANCE]"
            elif s >= 0.45:
                score_label = " [MEDIUM RELEVANCE]"
            else:
                score_label = " [LOW RELEVANCE]"

        parts.append(
            f"--- Passage {i}{score_label} ---\n"
            f"Topic: {doc['topic']}\n"
            f"Source: {doc['source_url']}\n"
            f"Content: {doc['text']}\n"
        )
    return "\n".join(parts)


def format_history(messages: list, max_turns: int = 4) -> str:
    """Format recent conversation history."""
    recent = messages[-(max_turns * 2):]
    if not recent:
        return "[No previous conversation.]"
    parts = []
    for msg in recent:
        role = "Student" if msg["role"] == "user" else "Assistant"
        parts.append(f"{role}: {msg['content']}")
    return "\n".join(parts)


def is_out_of_scope(question: str) -> bool:
    """Quick heuristic check — only rejects CLEARLY unrelated queries."""
    question_lower = question.lower()

    # Very strict: only reject if it matches these AND has zero connection to anything academic
    hard_reject_keywords = [
        "recipe", "cook", "weather forecast", "football score",
        "basketball score", "movie review", "song lyrics",
        "bitcoin price", "crypto", "stock price",
        "dating advice", "tell me a joke", "horoscope",
    ]

    # Anything even loosely related to internships/university/work should pass through
    pass_keywords = [
        "summer practice", "sp", "ie 300", "ie 400", "ie300", "ie400",
        "staj", "internship", "sgk", "insurance", "metu", "odtu",
        "report", "manual", "ocw", "evaluation", "committee",
        "practice", "industrial engineering", "form", "document",
        "company", "employer", "supervisor", "deadline",
        "abroad", "country", "erasmus", "europe", "work",
        "ulke", "yurtdisi", "sirket", "firma", "rapor",
        "belge", "sure", "hafta", "gun", "basvuru",
        "sigorta", "sozlesme", "contract", "letter", "mektup",
        "paid", "ucret", "maas", "voluntary", "gonullu",
        "register", "kayit", "enroll", "course", "ders",
        "grade", "not", "submit", "teslim", "upload",
        "student", "ogrenci", "department", "bolum",
        "faculty", "professor", "hoca", "office",
        "requirement", "gereksinim", "duration", "minimum",
        "project", "proje", "proposal", "public", "kamu",
        "foreign", "yabanci", "international", "bank", "banka",
        "service", "manufacturing", "hizmet", "uretim",
    ]

    has_pass = any(k in question_lower for k in pass_keywords)
    has_hard_reject = any(k in question_lower for k in hard_reject_keywords)

    # Only reject if hard reject AND absolutely no pass keyword
    return has_hard_reject and not has_pass
