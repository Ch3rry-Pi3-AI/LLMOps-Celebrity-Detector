# 🌟 **Celebrity Detection Module — LLMOps Celebrity Detector**

This branch introduces the first **LLM-powered recognition component** for the LLMOps Celebrity Detector.
It adds a complete utility for sending images to the Groq API and retrieving structured celebrity-identification output.

This marks the beginning of the model-driven reasoning layer that will eventually power the entire recognition workflow.

## 🗂️ **Project Structure (Updated)**

Only the **new** file introduced in this branch is annotated.

```text
LLMOPS-CELEBRITY-DETECTOR/
├── .circleci/
├── .venv/
├── app/
│   ├── __init__.py
│   └── utils/
│       ├── __init__.py
│       ├── image_handler.py
│       └── celebrity_detector.py          # NEW: Sends images to Groq API for celebrity identification
├── llmops_celebrity_detector.egg-info/
├── static/
├── templates/
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.py
└── uv.lock
```

## 🧠 **What This Branch Adds**

### `celebrity_detector.py`

A type-hinted, fully documented utility class that handles:

* Base64 encoding of image bytes
* Sending structured multimodal prompts to the Groq LLM API
* Parsing the model’s structured response
* Extracting the **Full Name** field automatically
* Providing a fallback value (“Unknown”) when identification fails

This module is designed to integrate directly with `image_handler.py` once the full face-to-celebrity pipeline is constructed.

### Key Features

* Straightforward API usage via the `identify()` method
* Clean structured response format
* Automatic extraction of name via `extract_name()`
* Strict separation of API communication from preprocessing logic
* Ready for integration with web routes or pipelines

## ⚙️ **Environment & Dependencies**

This branch requires:

* `requests` (already included in your dependencies)
* A valid Groq API key in `.env`:

```text
GROQ_API_KEY=""
```

No additional packages are needed.

Install dependencies with:

```bash
uv pip install -r requirements.txt
uv lock
```

## 📥 **Using the New Utility**

Import and instantiate:

```python
from app.utils.celebrity_detector import CelebrityDetector

detector = CelebrityDetector()
```

Send image bytes:

```python
result, name = detector.identify(image_bytes)
```

Return values:

* `result` → Full structured text response
* `name` → Extracted celebrity name or `"Unknown"`

## 🧩 **Integration Notes**

| Component               | Role                                                     |
| ----------------------- | -------------------------------------------------------- |
| `celebrity_detector.py` | Handles Groq API calls and structured celebrity output.  |
| `app/utils/`            | Shared helper utilities for preprocessing and LLM calls. |
| `app/`                  | Will later host routes, upload handlers, and UI logic.   |

## ✅ **In Summary**

This branch delivers the first **LLM reasoning module** for the LLMOps Celebrity Detector:

* Adds the complete celebrity-recognition utility
* Establishes API communication with Groq
* Provides structured output and automatic name extraction
* Prepares the system for full pipeline integration (image → face → celebrity)