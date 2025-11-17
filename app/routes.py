"""
routes.py

Flask route definitions for the LLMOps Celebrity Detector application.
Handles image uploads, celebrity identification, and follow-up Q&A interactions.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from flask import Blueprint, render_template, request
from app.utils.image_handler import process_image
from app.utils.celebrity_detector import CelebrityDetector
from app.utils.qa_engine import QAEngine
import base64


# --------------------------------------------------------------
# Blueprint Setup
# --------------------------------------------------------------
main = Blueprint("main", __name__)

# Initialise utilities once for reuse
celebrity_detector = CelebrityDetector()
qa_engine = QAEngine()


# --------------------------------------------------------------
# Routes
# --------------------------------------------------------------
@main.route("/", methods=["GET", "POST"])
def index():
    """
    Main route handling both image uploads and Q&A submissions.
    
    Returns
    -------
    Rendered HTML template with:
        player_info : str       → Celebrity info or LLM output
        result_img_data : str   → Annotated image encoded in base64
        user_question : str     → Question submitted by user
        answer : str            → LLM-generated answer
    """
    
    # Initialise all template variables
    player_info = ""
    result_img_data = ""
    user_question = ""
    answer = ""

    # ----------------------------------------------------------
    # Handle POST requests (image upload or Q&A)
    # ----------------------------------------------------------
    if request.method == "POST":

        # ----------------------------
        # Case 1: Image Upload
        # ----------------------------
        if "image" in request.files:
            image_file = request.files["image"]

            # Ensure file is present
            if image_file:
                # Process image and detect face
                img_bytes, face_box = process_image(image_file)

                # Identify celebrity using annotated or original bytes
                player_info, player_name = celebrity_detector.identify(img_bytes)

                # Encode image to base64 if a face was found
                if face_box is not None:
                    result_img_data = base64.b64encode(img_bytes).decode()
                else:
                    player_info = "No face detected. Please try another image."

        # ----------------------------
        # Case 2: Follow-up Question
        # ----------------------------
        elif "question" in request.form:
            user_question = request.form["question"]
            player_name = request.form["player_name"]
            player_info = request.form["player_info"]
            result_img_data = request.form["result_img_data"]

            # Ask follow-up question about identified celebrity
            answer = qa_engine.ask_about_celebrity(player_name, user_question)

    # ----------------------------------------------------------
    # Render HTML Template
    # ----------------------------------------------------------
    return render_template(
        "index.html",
        player_info=player_info,
        result_img_data=result_img_data,
        user_question=user_question,
        answer=answer
    )
