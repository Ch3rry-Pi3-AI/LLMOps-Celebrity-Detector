## 📁 **`utils/` — Core Utility Modules**

This folder contains reusable utility components for the **LLMOps Celebrity Detector**.
These modules provide foundational functionality that supports the main application logic, including image preprocessing, celebrity identification, and LLM-powered Q&A.

### 🔧 **Modules Included**

| File                    | Purpose                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ |
| `__init__.py`           | Marks the directory as a Python package.                                                                     |
| `image_handler.py`      | Loads images, decodes bytes, converts to grayscale, detects faces, and returns annotated output.             |
| `celebrity_detector.py` | Sends processed images to the Groq LLM API, retrieves structured celebrity data, and extracts the full name. |
| `qa_engine.py`          | Answers follow-up questions about identified celebrities using the Groq LLM API.                             |

### 🧩 **Overview**

The utilities in this folder are designed to be lightweight, modular, and easy to integrate across the project.
As the codebase grows, this directory will host additional helpers such as:

* Advanced image preprocessing tools
* Face embedding extractors
* Validation and sanitisation utilities
* Model I/O helpers
* Shared transformations and normalisers

### ✔️ **Usage**

You can import any utility like so:

```python
from app.utils.image_handler import process_image
from app.utils.celebrity_detector import CelebrityDetector
from app.utils.qa_engine import QAEngine
```

These modules can be used independently or together as part of a full image → face → identification → Q&A pipeline.