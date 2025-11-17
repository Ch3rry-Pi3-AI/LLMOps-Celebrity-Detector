"""
app.py

Root entrypoint for launching the Flask application used in the
LLMOps Celebrity Detector project. Loads environment variables,
initialises the Flask app via the factory pattern, and starts
the development server.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from app import create_app
from dotenv import load_dotenv


# --------------------------------------------------------------
# Application Entrypoint
# --------------------------------------------------------------
if __name__ == "__main__":
    load_dotenv()                     # Load environment variables from .env
    app = create_app()                # Create Flask application instance
    app.run(
        host="0.0.0.0",               # Allow external access (useful for containers)
        port=5000,                    # Default development port
        debug=True                    # Enable reload + debugging
    )
