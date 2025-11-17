# 📸 **Image Handling Module — LLMOps Celebrity Detector**

This branch adds the first functional component to the LLMOps Celebrity Detector:
a complete image-processing utility capable of decoding images, converting them into OpenCV format, detecting faces, and returning an annotated output.

This provides the foundation for all upcoming celebrity-recognition logic.

## 🗂️ **Project Structure (Updated)**

Only the **new** files for this branch are annotated.

```text
LLMOPS-CELEBRITY-DETECTOR/
├── .circleci/
├── .venv/
├── app/
│   ├── __init__.py
│   └── utils/
│       ├── __init__.py
│       └── image_handler.py               # NEW: Image decoding, preprocessing, face detection
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

### `image_handler.py`

A fully documented, type-hinted utility that performs:

* In-memory loading of uploaded images
* Conversion of raw bytes to NumPy
* OpenCV image decoding
* Grayscale conversion
* Face detection using Haar cascades
* Automatic selection of the **largest detected face**
* Drawing of bounding box annotations
* Returning:

  * Annotated JPEG bytes
  * A face bounding box `(x, y, w, h)` or `None`

This module now acts as the preprocessing stage for all face-based inference.

## ⚙️ **Environment & Dependencies**

No new external APIs or keys are required at this stage.
Haar cascades ship with OpenCV directly.

Install dependencies as normal:

```bash
uv pip install -r requirements.txt
uv lock
```

## 📥 **Using the New Utility**

Import anywhere inside the project:

```python
from app.utils.image_handler import process_image
```

Process an uploaded file:

```python
annotated_bytes, face_box = process_image(uploaded_file)
```

Returns:

* Annotated JPEG data
* Bounding box or `None`

## 🧩 **Integration Notes**

| Component          | Role                                                               |
| ------------------ | ------------------------------------------------------------------ |
| `image_handler.py` | Preprocessing, face detection, annotated image output.             |
| `app/utils/`       | Growing collection of helper modules (this branch adds the first). |
| `app/`             | Will later hold routes and celebrity-recognition logic.            |

## ✅ **In Summary**

This branch delivers:

* A complete image processing utility
* Modular and documented preprocessing logic
* Face detection foundation for later recognition stages
* Clean integration into the existing package structure

You can now move on to adding model inference, embedding extraction, routing logic, or UI components as your next branch.
