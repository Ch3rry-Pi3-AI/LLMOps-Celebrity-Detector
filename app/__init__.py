"""
__init__.py

Application factory for the LLMOps Celebrity Detector.
Initialises the Flask app, loads environment variables,
configures upload limits, and registers application blueprints.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from flask import Flask
from dotenv import load_dotenv
import os


# --------------------------------------------------------------
# Flask Application Factory
# --------------------------------------------------------------
def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns
    -------
    Flask
        The fully initialised Flask app instance.
    """
    
    load_dotenv()  # Load environment variables from .env

    # Resolve template directory (root/templates/)
    template_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "templates")
    )

    # Create the Flask app with custom template location
    app = Flask(__name__, template_folder=template_path)

    # Secret key for session handling (default used if not provided)
    app.secret_key = os.getenv("SECRET_KEY", "default_secret")

    # ----------------------------------------------------------
    # Request Size Configuration
    # ----------------------------------------------------------

    # Allow larger POST bodies for form fields (e.g., base64-encoded images)
    app.config["MAX_FORM_MEMORY_SIZE"] = 5 * 1024 * 1024   # 5 MB

    # Optional: Increase total request size limit
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024    # 16 MB

    # ----------------------------------------------------------
    # Register Blueprints
    # ----------------------------------------------------------
    from app.routes import main
    app.register_blueprint(main)

    return app
