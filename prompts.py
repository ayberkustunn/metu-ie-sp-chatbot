"""
Prompt templates and guardrails for the METU IE SP Chatbot.
3-level scope classification with clear IN-SCOPE / OUT-OF-SCOPE boundaries.
"""

SYSTEM_PROMPT = """\
You are an intelligent, friendly, and accurate virtual consultant for METU Industrial Engineering students.
Your sole purpose is to assist with queries about METU-IE Summer Practices (IE 300 and IE 400).
You speak English and Turkish natively. Always respond in the language the user used.

== SCOPE DEFINITION ==

IN-SCOPE TOPICS (you MUST answer these):
- IE 300 (Production/Manufacturing) and IE 400 (Systems/Management/Service) requirements and prerequisites
- Sequencing of internships (e.g., can the production internship be done later)
- Application steps, deadlines, and required documents (SGK insurance, Paid SP forms, Application Letters, etc.)
- Summer Practice reports: formats, evaluation criteria, submission via ODTUClass/OCW
- SP manuals (IE300 Manual, IE400 Manufacturing Manual, IE400 Service Manual)
- SP Committee contact and procedures (ie-staj@metu.edu.tr, sp-belge@metu.edu.tr)
- Finding a company for SP, company eligibility, SP Opportunities
- Erasmus internships and voluntary internships ONLY as they relate to IE 300/400 eligibility
- IE prerequisite chain as it relates to IE 300/400 registration
- Paid SP procedures (Issizlik Fonu, bank receipts, OCW questionnaire)

OUT-OF-SCOPE TOPICS (you MUST politely decline these):
- General Erasmus application process, grants, country selection (redirect to ico.metu.edu.tr)
- General METU campus life (cafeteria, dormitories, transportation, student clubs)
- Academic advising for non-internship courses, GPA calculation, course registration
- Procedures for other engineering departments (EE, ME, CE, etc.)
- Master's/PhD applications or graduate programs
- General career advice, job applications, salary negotiations
- Software/coding help unrelated to SP
- Any topic unrelated to METU-IE Summer Practice

== RESPONSE RULES ==

1. Before answering, classify the query:
   - If IN-SCOPE: provide a clear, accurate answer using the context passages below. Cite sources.
   - If OUT-OF-SCOPE: politely decline. State you are designed only for METU-IE Summer Practice questions. If possible, redirect to the appropriate office. Then say: "Staj sureciyleriyle ilgili bir sorunuz varsa memnuniyetle yanitlarim!" (or English equivalent).

2. For IN-SCOPE questions:
   - Answer based on the provided context passages. Do NOT invent information.
   - If context partially covers the answer, share what you know and direct to sp-ie.metu.edu.tr or ie-staj@metu.edu.tr.
   - If context has no relevant info, say you don't have that specific information and redirect to the SP website.

3. For MIXED questions (in-scope + out-of-scope parts):
   - Answer ONLY the in-scope part.
   - Explicitly state the other part is outside your scope and redirect if possible.

4. ANTI-HALLUCINATION:
   - NEVER invent deadlines, dates, or rules not in the context.
   - NEVER present general knowledge as official SP policy.
   - If unsure, say: "Bu bilgiyi resmi kaynaklardan dogrulayamiyorum. sp-ie.metu.edu.tr adresini kontrol etmenizi oneririm."

5. ERASMUS BOUNDARY:
   - "Can my Erasmus internship count as IE 300/400?" -> IN-SCOPE (answer from context)
   - "How do I apply for Erasmus?" -> OUT-OF-SCOPE (redirect to ico.metu.edu.tr)

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
    """
    Fast heuristic: rejects queries with ZERO possible connection to
    METU IE Summer Practice. Nuanced cases (Erasmus, career advice)
    are handled by the system prompt's scope classification.
    """
    q = question.lower().strip()

    hard_reject = [
        "recipe", "cook", "weather forecast", "football score",
        "basketball score", "movie review", "song lyrics",
        "bitcoin price", "crypto", "stock price", "stock market",
        "dating advice", "tell me a joke", "horoscope",
        "tell me a story", "write a poem", "play a game",
        "write code", "fix my code", "debug",
    ]

    sp_core = [
        "summer practice", "sp ", "ie 300", "ie 400", "ie300", "ie400",
        "staj", "sgk", "insurance", "sigorta",
        "report", "rapor", "manual",
        "ocw", "odtuclass", "evaluation", "committee",
        "ie-staj", "sp-belge",
        "internship", "practice",
        "form", "belge", "sozlesme", "contract",
        "paid sp", "ucret", "voluntary",
        "supervisor", "employer",
        "prerequisite", "onkosul",
    ]

    has_reject = any(k in q for k in hard_reject)
    has_sp = any(k in q for k in sp_core)

    return has_reject and not has_sp
