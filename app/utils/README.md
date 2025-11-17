## 📁 **`utils/` — Core Utility Modules**

This folder contains reusable utility components for the **LLMOps Celebrity Detector**.
These modules provide foundational functionality that supports the main application logic.

### 🔧 **Modules Included**

| File               | Purpose                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| `__init__.py`      | Marks the directory as a Python package.                                                                |
| `image_handler.py` | Handles image loading, decoding, grayscale conversion, face detection, and annotated output generation. |

### 🧩 **Overview**

The utilities in this folder are designed to be lightweight, modular, and easy to integrate across the project.
As the codebase grows, this directory will host additional helpers such as:

* Image preprocessing tools
* Validation and sanitisation utilities
* Model I/O helpers
* Common transformations

### ✔️ **Usage**

All utilities can be imported using:

```python
from app.utils.image_handler import process_image
```
