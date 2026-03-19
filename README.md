# METU IE Summer Practice Chatbot 🎓

An intelligent RAG-based chatbot that answers questions about **METU Industrial Engineering Summer Practices** (IE 300 / IE 400), built for **IE 304 – Project 1**.

## Architecture

```
User Question
     │
     ▼
┌─────────────┐     ┌──────────────────┐     ┌────────────────┐
│  Streamlit   │────▶│  Out-of-Scope    │────▶│  FAISS Vector  │
│  Chat UI     │     │  Guardrail       │     │  Search        │
└─────────────┘     └──────────────────┘     └───────┬────────┘
                                                      │
                                              Top-k documents
                                                      │
                                                      ▼
                                             ┌────────────────┐
                                             │  GPT-4o-mini   │
                                             │  (grounded     │
                                             │   generation)  │
                                             └───────┬────────┘
                                                      │
                                              Answer + Sources
                                                      │
                                                      ▼
                                                   Student
```

**Components:**
- **Knowledge Base** (`knowledge_base.py`): 30+ structured chunks extracted from [sp-ie.metu.edu.tr/en](https://sp-ie.metu.edu.tr/en) plus curated FAQ
- **Retriever** (`retriever.py`): FAISS vector index using OpenAI `text-embedding-3-small`, with keyword fallback
- **Prompts & Guardrails** (`prompts.py`): System prompt enforcing grounded answers, out-of-scope detection, source citation
- **App** (`app.py`): Streamlit chat interface with conversation history

## Quick Start (Local)

```bash
# 1. Clone the repository
git clone https://github.com/ayberkustunn/metu-ie-sp-chatbot.git
cd metu-ie-sp-chatbot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your OpenAI API key
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml and add your key

# 4. Run
streamlit run app.py
```

## Deployment on Streamlit Cloud

1. Push the code to a **public GitHub repository**.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"New app"** → select your repo, branch `main`, and file `app.py`.
4. Go to **"Advanced settings" → "Secrets"** and add:
   ```
   OPENAI_API_KEY = "sk-your-key-here"
   ```
5. Click **"Deploy"**. The app will be live at `https://<your-app>.streamlit.app`.

## Project Structure

```
metu-ie-sp-chatbot/
├── app.py                 # Streamlit main application
├── knowledge_base.py      # Structured content from SP website
├── retriever.py           # FAISS vector search + keyword fallback
├── prompts.py             # System prompts and guardrails
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── .streamlit/
    ├── config.toml        # Streamlit theme configuration
    └── secrets.toml.example  # API key template
```

## Testing

Try these queries to evaluate the chatbot:

| # | Query | Expected Behavior |
|---|-------|-------------------|
| 1 | "How do I apply for SGK insurance?" | Step-by-step OCW procedure with source |
| 2 | "What are the requirements for IE 300?" | Duration, physical attendance, manual reference |
| 3 | "Can I do my internship remotely?" | Clear "no" — physical attendance required |
| 4 | "What is the weather today?" | Out-of-scope rejection |
| 5 | "Who do I contact for SP questions?" | ie-staj@metu.edu.tr, sp-belge@metu.edu.tr |

## Data Source

All information is extracted from the official METU IE Summer Practice website:
**https://sp-ie.metu.edu.tr/en**

Pages covered: Home, General Information, Steps to Follow, Documents/Forms, FAQ, SP Committee, SP Opportunities.

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-4o-mini
- **Embeddings**: OpenAI text-embedding-3-small
- **Vector Store**: FAISS (in-memory)
- **Hosting**: Streamlit Cloud

## License

Academic project — IE 304, METU Industrial Engineering Department.
