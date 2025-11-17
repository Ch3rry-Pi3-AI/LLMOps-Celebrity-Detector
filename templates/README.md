# 🎨 **`templates/` — Front-End HTML Templates**

The `templates/` directory contains all Jinja2-based HTML templates used by the **LLMOps Celebrity Detector** web interface.
These templates define the visual structure of the application, rendering:

* Uploaded images
* Detected celebrity information
* Follow-up Q&A responses
* Upload and question forms

This folder is tightly integrated with the Flask routing layer and forms the user-facing part of the system.

## 📁 **Folder Structure**

```text
templates/
└── index.html
```

## 🧩 **Components**

### `index.html`

The main UI template for the project.
It provides the full workflow:

* Image upload form
* Base64-rendered annotated image
* Parsed celebrity information from the LLM
* A follow-up Q&A form
* Display of generated answers

The page uses:

* **TailwindCSS** for styling
* **Jinja2** for dynamic content rendering
* A minimal local stylesheet via `static/style.css`

Docstrings and comment blocks are included for clarity and maintainability.

## 🚀 **Purpose of the `templates/` Layer**

This folder defines the complete front-end experience of the LLMOps Celebrity Detector.
It connects directly with:

* `routes.py` — sends values to templates
* `image_handler.py` — provides annotated image bytes
* `celebrity_detector.py` — supplies structured celebrity info
* `qa_engine.py` — generates answers for Q&A

This ensures a clear separation between application logic and visual presentation.

## ✔️ **Usage Example**

In your Flask route:

```python
return render_template(
    "index.html",
    player_info=player_info,
    result_img_data=result_img_data,
    user_question=user_question,
    answer=answer
)
```

The template receives dynamic data through Jinja variables, enabling responsive, real-time rendering of recognition results and Q&A interaction.
