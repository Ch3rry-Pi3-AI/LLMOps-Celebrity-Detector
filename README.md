# 💬 **Celebrity Q&A Module — LLMOps Celebrity Detector**

This branch introduces the **Q&A reasoning layer** for the LLMOps Celebrity Detector.
It adds a dedicated utility for asking follow-up questions about a recognised celebrity using the Groq LLM API.

With this module, the system now supports a full conversational step after identification, enabling richer interactions and deeper insights.

## 🗂️ **Project Structure (Updated)**

Only the **new** file added in this branch is annotated.

```text
LLMOPS-CELEBRITY-DETECTOR/
├── .circleci/
├── .venv/
├── app/
│   ├── __init__.py
│   └── utils/
│       ├── __init__.py
│       ├── image_handler.py
│       ├── celebrity_detector.py
│       └── qa_engine.py                  # NEW: LLM-powered Q&A engine for celebrity questions
├── llmops_celebrity_detector.egg-info/
├── static/
├── templates/
├── .env
├── .gitignore/
├── .python-version
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.py
└── uv.lock
```

## 🧠 **What This Branch Adds**

### `qa_engine.py`

A clean, type-hinted, fully documented utility class that enables:

* Asking natural-language questions about a specific celebrity
* Generating concise, accurate answers using the Groq LLM API
* Automatic prompt construction using the celebrity’s name
* Graceful fallback messaging if the API request fails

This module connects directly with the output of `celebrity_detector.py`, forming the **celebrity → facts → Q&A** workflow.

### Key Features

* Simple `ask_about_celebrity()` interface
* Injects celebrity name dynamically into the prompt
* Uses the same model as the detection module for consistency
* Seamlessly integrates into future routes or interfaces

## ⚙️ **Environment & Dependencies**

This branch requires:

* `requests` (already in your project)
* A valid Groq API key set in `.env`:

```text
GROQ_API_KEY=""
```

Install dependencies:

```bash
uv pip install -r requirements.txt
uv lock
```

## 📥 **Using the New Utility**

Import and create an instance:

```python
from app.utils.qa_engine import QAEngine

qa = QAEngine()
```

Ask a question:

```python
answer = qa.ask_about_celebrity("Tom Cruise", "What awards has he won?")
```

Return value:

* `answer` → A concise LLM-generated response, or a fallback message.

## 🧩 **Integration Notes**

| Component               | Role                                                         |
| ----------------------- | ------------------------------------------------------------ |
| `qa_engine.py`          | Handles follow-up question answering via Groq LLM API.       |
| `celebrity_detector.py` | Supplies the celebrity name used for Q&A prompts.            |
| `app/utils/`            | Shared helper layer for core reasoning and preprocessing.    |
| `app/`                  | Will later host routes, views, and interactive Q&A features. |

## ✅ **In Summary**

This branch introduces the **first conversational reasoning module** for the LLMOps Celebrity Detector:

* Adds a complete LLM-driven Q&A engine
* Extends the pipeline beyond identification into interactive dialogue
* Provides clean modular design for future UI and API layers

The project can now support a full flow:
**image → face detection → celebrity identification → follow-up Q&A**.