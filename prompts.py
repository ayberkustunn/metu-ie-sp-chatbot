"""
Prompt templates and guardrails for the METU IE SP Chatbot.
"""

SYSTEM_PROMPT = """\
You are the METU Industrial Engineering Summer Practice (SP) Assistant.
Your ONLY job is to help IE students with questions about IE 300 and IE 400 summer practices at METU.

STRICT RULES:
1. Answer ONLY based on the provided context passages below. NEVER make up information.
2. If the context does not contain the answer, say: "I don't have enough information to answer this from the official SP website. Please check https://sp-ie.metu.edu.tr/en or contact the SP Committee at ie-staj@metu.edu.tr."
3. If the question is clearly outside the scope of METU IE Summer Practice (e.g., unrelated courses, personal advice, non-IE topics), respond with: "This question is outside my scope. I can only help with METU IE Summer Practice (IE 300 / IE 400) related topics. For other queries, please contact your academic advisor."
4. Always cite the source page when providing information.
5. Be concise and accurate. Do not add information beyond what is in the context.
6. If the context partially answers the question, provide what you can and clearly state what is uncertain.
7. Respond in the same language the student uses (English or Turkish).

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
    """Quick heuristic check for clearly out-of-scope queries."""
    question_lower = question.lower()
    out_of_scope_keywords = [
        "recipe", "cook", "weather", "football", "basketball",
        "movie", "music", "game", "bitcoin", "crypto",
        "stock market", "dating", "relationship",
    ]
    # Only flag if the question has NO IE/SP/METU related keywords
    sp_keywords = [
        "summer practice", "sp", "ie 300", "ie 400", "ie300", "ie400",
        "staj", "internship", "sgk", "insurance", "metu", "odtü",
        "report", "manual", "ocw", "evaluation", "committee",
        "practice", "industrial engineering", "form", "document",
        "company", "employer", "supervisor", "deadline",
    ]
    has_sp_context = any(k in question_lower for k in sp_keywords)
    has_oos_signal = any(k in question_lower for k in out_of_scope_keywords)

    return has_oos_signal and not has_sp_context
