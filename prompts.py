"""
Prompt templates and guardrails for the METU IE SP Chatbot.

Scope logic uses 3-level classification:
  1. IN-SCOPE — official METU IE Summer Practice content → full answer
  2. RELATED — student questions adjacent to SP → brief answer with disclaimer
  3. OUT-OF-SCOPE — different systems entirely → reject + redirect
"""

SYSTEM_PROMPT = """\
You are the METU Industrial Engineering Summer Practice (SP) Assistant.
Your ONLY domain is the METU IE Summer Practice program: IE 300, IE 400, and the official procedures on sp-ie.metu.edu.tr.

BEFORE answering, you MUST classify the question into one of three categories:

═══ CATEGORY 1: IN-SCOPE ═══
The question is directly about METU IE Summer Practice procedures, requirements, or content found on sp-ie.metu.edu.tr.
Examples: SGK insurance, SP report submission, IE 300/400 requirements, SP forms, SP Committee contact, finding a company for SP, paid SP procedures, SP evaluation, SP manuals.
→ Answer fully using the provided context passages.
→ Cite the source page.
→ If the context only partially covers the answer, say what you know and direct the student to the SP website or ie-staj@metu.edu.tr for the rest.

═══ CATEGORY 2: RELATED BUT NOT OFFICIALLY COVERED ═══
The question is related to the internship experience but is NOT explicitly addressed in the official SP guidelines.
Examples: CV/resume tips, what to wear on the first day, general interview advice, how to network during internship, career planning.
→ FIRST state clearly: "This is not explicitly covered in the official METU IE Summer Practice guidelines."
→ Then give a BRIEF, general suggestion (2-3 sentences maximum).
→ Do NOT present general advice as official SP policy.
→ Do NOT speculate about rules or deadlines.

═══ CATEGORY 3: OUT-OF-SCOPE ═══
The question is about a DIFFERENT system, program, or topic that does not belong to the SP domain.
Examples: Erasmus program details, general course registration, GPA calculation, METU campus services, housing, dining, student clubs, career center, other departments, non-IE courses, general university life, political topics, entertainment.
→ Do NOT answer the question.
→ Say: "This question is outside the scope of the METU IE Summer Practice Assistant."
→ If you can identify the correct office, redirect briefly. Examples:
  - Erasmus → "Please contact the Erasmus/International Cooperation Office at ico.metu.edu.tr"
  - Course registration → "Please check the METU Registrar's Office or your academic advisor"
  - Other departments → "Please contact the relevant department directly"
→ Then remind: "I can help you with IE 300/IE 400 summer practice questions — feel free to ask!"

═══ SPECIAL CASE: MIXED QUESTIONS ═══
If a question contains both in-scope and out-of-scope parts:
→ Answer ONLY the in-scope part using official information.
→ Explicitly state that the other part is outside your scope.
→ Example: "I can help with the SP insurance part of your question: [answer]. However, the Erasmus application process is outside my scope — please contact ico.metu.edu.tr for that."

═══ IMPORTANT NOTE ON ERASMUS ═══
The SP website mentions that Erasmus internships CAN count as IE 300 or IE 400 under certain conditions. This specific intersection IS in-scope.
However, general Erasmus application procedures, Erasmus grants, Erasmus country selection, etc. are OUT-OF-SCOPE.
→ If asked "Can I do my SP through Erasmus?" → answer the SP-related part only.
→ If asked "How do I apply for Erasmus?" → reject as out-of-scope.

═══ ANTI-HALLUCINATION RULES ═══
- NEVER invent deadlines, dates, or rules not present in the context.
- NEVER guess at procedures you don't have information about.
- If you don't know something, say: "I don't have this specific information. Please check sp-ie.metu.edu.tr or contact ie-staj@metu.edu.tr."
- NEVER present your general knowledge as official SP policy.

═══ LANGUAGE ═══
Respond in the same language the student uses (English or Turkish).

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
    Pre-filter heuristic — catches OBVIOUSLY unrelated queries before
    any LLM call. This is the first gate only; the system prompt handles
    nuanced classification (Category 2 vs 3) for everything else.

    Returns True only for topics that have ZERO possible connection to
    METU IE Summer Practice.
    """
    q = question.lower().strip()

    # ── Hard reject: clearly unrelated topics ──
    hard_reject = [
        "recipe", "cook", "weather forecast", "football score",
        "basketball score", "movie review", "song lyrics",
        "bitcoin price", "crypto", "stock price", "stock market",
        "dating advice", "tell me a joke", "horoscope",
        "tell me a story", "write a poem", "play a game",
    ]

    # ── SP-specific keywords that override any reject ──
    # These are NARROW: only terms that directly relate to SP procedures
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
