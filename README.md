# 🌐 **Web Routing Layer — LLMOps Celebrity Detector**

This branch introduces the first **application-layer routing** for the LLMOps Celebrity Detector.
It adds a Flask route handler that ties together the entire workflow:

**image → face detection → celebrity identification → follow-up Q&A**

This creates the foundation for the project’s interactive web interface and enables users to upload images, view results, and ask questions in a single unified page.

## 🗂️ **Project Structure (Updated)**

Only the **new** file added in this branch is annotated.

```text
LLMOPS-CELEBRITY-DETECTOR/
├── .circleci/
├── .venv/
├── app/
│   ├── __init__.py
│   ├── routes.py                         # NEW: Main Flask routes for image upload + Q&A
│   └── utils/
│       ├── __init__.py
│       ├── image_handler.py
│       ├── celebrity_detector.py
│       └── qa_engine.py
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

### `routes.py`

A fully formatted and structured Flask routing layer that:

* Accepts uploaded images via POST
* Runs full preprocessing through `process_image()`
* Identifies the detected face using `CelebrityDetector`
* Encodes annotated images as base64 for display
* Handles user-submitted follow-up questions
* Pipes Q&A requests to `QAEngine`
* Renders results cleanly via `index.html`

This file acts as the central controller that orchestrates all utilities and drives the application flow.

### Key Features

* Clean separation of GET and POST handling
* Intuitive flow for both image and question submission
* Reuse of instantiated utilities (no repeated initialisation)
* Ready for integration with the UI templates

## ⚙️ **Environment & Dependencies**

This branch introduces **no new dependencies**.

Requirements remain:

* Flask
* OpenCV
* Requests
* A valid Groq API key:

```text
GROQ_API_KEY=""
```

Install dependencies if needed:

```bash
uv pip install -r requirements.txt
uv lock
```

## 📥 **Using the New Route**

When the Flask app is initialised, register the blueprint:

```python
from app.routes import main
app.register_blueprint(main)
```

The route behaves as follows:

### 1. User uploads an image

* System detects face
* Identifies celebrity
* Displays annotated image
* Shows structured recognition output

### 2. User asks a question

* Q&A engine is triggered
* Answer appears beneath the result

## 🧩 **Integration Notes**

| Component               | Role                                                         |
| ----------------------- | ------------------------------------------------------------ |
| `routes.py`             | Application controller for uploads, identification, and Q&A. |
| `image_handler.py`      | Preprocesses images and detects faces.                       |
| `celebrity_detector.py` | Performs LLM-powered celebrity identification.               |
| `qa_engine.py`          | Handles follow-up Q&A about recognised celebrities.          |
| `templates/`            | Renders the resulting information to the user.               |

## ✅ **In Summary**

This branch introduces the **application orchestration layer**, enabling:

* User interaction through the browser
* Full processing pipeline execution
* Dynamic Q&A based on detected celebrities
* Smooth integration between utilities and UI

With routing now in place, the project is ready for the next stage:
**HTML template development and front-end interaction.**
