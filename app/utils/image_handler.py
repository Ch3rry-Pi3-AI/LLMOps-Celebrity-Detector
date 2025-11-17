"""
image_handler.py

Utility module for processing uploaded images and detecting faces using OpenCV.
Provides functionality to extract image bytes, convert to arrays,
detect the largest face, and return an annotated result.

Functions
---------
process_image(image_file)
    Processes an uploaded image, detects faces, and returns the
    annotated image bytes along with bounding box coordinates.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
import cv2
from io import BytesIO
import numpy as np
from typing import Tuple, Optional, Any


# --------------------------------------------------------------
# Image Processing Function
# --------------------------------------------------------------
def process_image(image_file: Any) -> Tuple[bytes, Optional[Tuple[int, int, int, int]]]:
    """
    Process an uploaded image and detect the largest face.

    This function:
    1. Reads a file-like object into memory
    2. Converts it into a NumPy array
    3. Decodes it into an OpenCV image
    4. Converts the image to grayscale
    5. Detects faces using Haar cascades
    6. Draws a bounding box around the largest detected face
    7. Returns annotated image bytes and face coordinates

    Parameters
    ----------
    image_file : file-like object
        The uploaded image object. Must support `.save()`.

    Returns
    -------
    tuple
        annotated_bytes : bytes
            The processed image encoded as JPEG bytes.
            If no face is detected, returns the original image bytes.
        largest_face : tuple of int or None
            Bounding box `(x, y, w, h)` of the largest detected face.
            Returns None when no face is detected.

    Notes
    -----
    OpenCV's Haar cascades work best on front-facing human faces
    in well-lit conditions. Detection performance varies depending
    on angle, lighting, and image resolution.
    """

    # ----------------------------------------------------------
    # Load uploaded image into an in-memory buffer
    # ----------------------------------------------------------
    in_memory_file = BytesIO()        # Create a byte buffer for the file
    image_file.save(in_memory_file)   # Save the upload into the buffer

    # Retrieve raw bytes from the in-memory file
    image_bytes: bytes = in_memory_file.getvalue()

    # Convert raw bytes to a NumPy array for OpenCV
    nparr: np.ndarray = np.frombuffer(image_bytes, np.uint8)

    # ----------------------------------------------------------
    # Decode image and convert to grayscale
    # ----------------------------------------------------------
    img: np.ndarray = cv2.imdecode(nparr, cv2.IMREAD_COLOR)    # Convert bytes → image
    gray: np.ndarray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # Convert to grayscale

    # ----------------------------------------------------------
    # Load Haar cascade and detect faces
    # ----------------------------------------------------------
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )   # Haar cascade for face detection

    faces: np.ndarray = face_cascade.detectMultiScale(gray, 1.1, 5)  # Detect faces

    # If no faces detected, return original bytes
    if len(faces) == 0:
        return image_bytes, None

    # ----------------------------------------------------------
    # Identify the largest detected face
    # ----------------------------------------------------------
    largest_face: Tuple[int, int, int, int] = max(
        faces, key=lambda r: r[2] * r[3]
    )   # Select by area (w*h)
    (x, y, w, h) = largest_face         # Unpack bounding box

    # ----------------------------------------------------------
    # Draw bounding box around detected face
    # ----------------------------------------------------------
    cv2.rectangle(
        img,               # Image to draw on
        (x, y),            # Top-left corner
        (x + w, y + h),    # Bottom-right corner
        (0, 255, 0),       # Green bounding box
        3                  # Thickness
    )

    # ----------------------------------------------------------
    # Encode the modified image as JPEG and return bytes
    # ----------------------------------------------------------
    is_success: bool
    buffer: np.ndarray
    is_success, buffer = cv2.imencode(".jpg", img)   # Encode final result

    return buffer.tobytes(), largest_face
