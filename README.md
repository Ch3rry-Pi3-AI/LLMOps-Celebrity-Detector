# 🌐 **Flask Application Layer — LLMOps Celebrity Detector**

This branch introduces the **full Flask application layer** for the LLMOps Celebrity Detector.
It connects all previously built components — image preprocessing, celebrity recognition, and Q&A — into a complete, interactive web application.

This is the first branch where users can run the project end-to-end through a browser interface.

## 🗂️ **Project Structure (Updated)**

Only the **new** files introduced in this branch are annotated.

```text
LLMOPS-CELEBRITY-DETECTOR/
├── .circleci/
├── .venv/
├── app/
│   ├── __init__.py                    # NEW: Flask application factory (app setup & blueprint registration)
│   ├── routes.py
│   └── utils/
│       ├── __init__.py
│       ├── image_handler.py
│       ├── celebrity_detector.py
│       └── qa_engine.py
├── static/
│   └── style.css                      # NEW: Custom CSS (animations, glow effects, transitions)
├── templates/
│   └── index.html                     # NEW: Main UI template for uploads, results & Q&A
├── app.py                             # NEW: Root application entrypoint (runserver)
├── llmops_celebrity_detector.egg-info/
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

### `app.py` (root entrypoint)

A clean application launcher that:

* Loads environment variables
* Calls `create_app()` to initialise Flask
* Runs the app with debugging enabled
* Exposes the server on `0.0.0.0:5000`

This is now the main command for starting the project:

```bash
python app.py
```

### `app/__init__.py` (Flask application factory)

Creates and configures the Flask app:

* Loads environment variables
* Registers template directory
* Sets secret key
* Configures POST/request size limits
* Registers the `main` blueprint

This ensures the project remains modular and scalable.

### `templates/index.html`

The main UI for the entire system:

* Image upload form
* Base64 rendering of annotated detection images
* Parsed celebrity information (name, profession, nationality, etc.)
* Follow-up Q&A input
* Animated and responsive layout powered by TailwindCSS
* Custom glow, fade, and hover effects

### `static/style.css`

The custom styling layer for the front-end:

* Solid black background
* Neon rose glowing title
* Button + image hover transitions
* Gradient “answer box”
* Smooth fade-in animations
* Visual polish on top of TailwindCSS

## ✨ **Key Features of This Branch**

* Full web app now runs end-to-end
* Tight connection between UI, preprocessing, and reasoning
* Clean separation of responsibilities:

  * `app.py` → entrypoint
  * `__init__.py` → configuration
  * `routes.py` → business logic
  * `index.html` → rendering
  * `style.css` → visual presentation
* All components integrated into a functional workflow
* A polished, modern UI with animation and glow effects

## ⚙️ **Environment & Dependencies**

No new Python dependencies beyond what the earlier branch required.

Ensure:

```text
GROQ_API_KEY=""
SECRET_KEY=""
```

Install dependencies (if not yet installed):

```bash
uv pip install -r requirements.txt
uv lock
```

## 📥 **Running the Application**

From the project root:

```bash
python app.py
```

Then open:

```
http://localhost:5000
```

You can now:

1. Upload an image
2. See the detected face + LLM identification
3. Ask follow-up questions
4. View the generated responses

## 🧩 **Integration Notes**

| Component     | Role                                                   |
| ------------- | ------------------------------------------------------ |
| `app.py`      | Launches the Flask server.                             |
| `__init__.py` | Creates & configures the Flask application.            |
| `routes.py`   | Handles uploads, recognition, Q&A, and view rendering. |
| `index.html`  | Renders the full UI.                                   |
| `style.css`   | Provides animations, glow effects, and UI polish.      |

## ✅ **In Summary**

This branch delivers the **complete Flask application layer**, allowing the entire LLMOps Celebrity Detector to run interactively in a browser.

You now have:

* A full working web interface
* Centralised app configuration
* Clean blueprint-based routing
* Responsive, animated front-end styling
* A polished user experience
