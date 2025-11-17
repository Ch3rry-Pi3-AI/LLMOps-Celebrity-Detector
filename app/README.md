# 🎛️ **`app/` — Application Layer**

The `app/` directory contains the main application logic for the **LLMOps Celebrity Detector**.
It serves as the central layer where routing, request handling, and core utility modules come together to provide the full user-facing functionality.

This folder will eventually expand to include the complete web interface, API endpoints, and orchestration logic that links image processing, celebrity recognition, and Q&A generation.

## 📁 **Folder Structure**

```text
app/
├── __init__.py
├── routes.py
└── utils/
    ├── __init__.py
    ├── image_handler.py
    ├── celebrity_detector.py
    └── qa_engine.py
```

## 🧩 **Components**

### `routes.py`

Handles web routes for the application, including:

* Uploading images
* Running face detection
* Performing celebrity identification
* Sending follow-up questions to the Q&A engine
* Rendering results in the HTML template

### `utils/`

Contains core helper modules powering the application:

* `image_handler.py` — Image decoding, preprocessing, and face detection
* `celebrity_detector.py` — LLM-powered celebrity identification
* `qa_engine.py` — Answers follow-up questions about recognised celebrities

Each module is independently usable and designed to integrate seamlessly into the routing layer.

## 🚀 **Purpose of the `app/` Layer**

The `app/` folder acts as the glue that connects:

* Front-end templates
* User uploads
* Utility functions
* LLM reasoning modules
* Future endpoints and orchestration logic

It ensures the project grows in an organised, modular, and scalable way.

## ✔️ **Usage Example**

From the project root, the application is launched through your Flask entrypoint (created in a later branch), with logic delegated to:

```python
from app.routes import main
```

Utilities are imported cleanly thanks to package structure:

```python
from app.utils.celebrity_detector import CelebrityDetector
from app.utils.qa_engine import QAEngine
```