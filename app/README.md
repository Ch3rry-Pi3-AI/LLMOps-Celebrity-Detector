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

### `__init__.py`

Implements the Flask **application factory**, responsible for:

* Loading environment variables
* Locating and configuring the template directory
* Setting secret keys and request-size limits
* Registering blueprints (including the main route handler)
* Returning a fully initialised Flask app

This file defines how the entire web application is constructed and ensures a clean, scalable architecture.

### `routes.py`

Handles the primary web routes for the project, including:

* Uploading images
* Running face detection
* Performing celebrity identification
* Sending follow-up questions to the Q&A engine
* Rendering results via the HTML template

### `utils/`

Contains helper modules powering the application:

* `image_handler.py` — Image decoding, preprocessing, and face detection
* `celebrity_detector.py` — LLM-powered celebrity identification
* `qa_engine.py` — Answers follow-up questions about recognised celebrities

Each utility is independently usable and designed to integrate seamlessly into the routing layer.

## 🚀 **Purpose of the `app/` Layer**

The `app/` folder acts as the glue that connects:

* Front-end templates
* User uploads
* Utility functions
* LLM reasoning modules
* Future API endpoints and interfaces

It ensures the project evolves in a structured, modular, and scalable way.

## ✔️ **Usage Example**

From the project root, the application runs through the Flask entrypoint:

```python
from app import create_app
```

Routes are registered automatically through the application factory:

```python
from app.routes import main
```

Utility modules are imported cleanly:

```python
from app.utils.celebrity_detector import CelebrityDetector
from app.utils.qa_engine import QAEngine
```