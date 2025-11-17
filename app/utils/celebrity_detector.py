"""
celebrity_detector.py

Utility module for identifying celebrities using the Groq LLM API.
Provides functionality for sending base64-encoded images to the model
and extracting structured identification results.

Classes
-------
CelebrityDetector
    Handles API communication and celebrity name extraction.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
import os
import base64
import requests
from typing import Tuple, Optional


# --------------------------------------------------------------
# Celebrity Detection Class
# --------------------------------------------------------------
class CelebrityDetector:
    """
    A utility class for identifying celebrities using the Groq LLM API.

    Methods
    -------
    identify(image_bytes)
        Sends an image to the LLM endpoint and returns the structured response.
    extract_name(content)
        Extracts the celebrity's full name from the model's response.
    """

    def __init__(self) -> None:
        """Initialise API credentials and model configuration."""
        self.api_key: Optional[str] = os.getenv("GROQ_API_KEY")          # Load API key from environment
        self.api_url: str = "https://api.groq.com/openai/v1/chat/completions"
        self.model: str = "meta-llama/llama-4-maverick-17b-128e-instruct"

    # ----------------------------------------------------------
    # Send image to Groq + LLM Response Handling
    # ----------------------------------------------------------
    def identify(self, image_bytes: bytes) -> Tuple[str, str]:
        """
        Identify the celebrity in the provided image.

        Parameters
        ----------
        image_bytes : bytes
            Raw JPEG image data.

        Returns
        -------
        tuple
            result : str
                Full structured response from the LLM.
            name : str
                Extracted celebrity name, or "Unknown" if undetected.
        """

        # Encode the raw image bytes as base64 for transmission
        encoded_image: str = base64.b64encode(image_bytes).decode()

        # Prepare request headers for the API call
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Construct the message prompt for the LLM
        prompt = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            # Instructions for structured celebrity identification
                            "type": "text",
                            "text": (
                                "You are a celebrity recognition expert AI.\n"
                                "Identify the person in the image. If known, respond in this format:\n\n"
                                "- **Full Name**:\n"
                                "- **Profession**:\n"
                                "- **Nationality**:\n"
                                "- **Famous For**:\n"
                                "- **Top Achievements**:\n\n"
                                "If unknown, return \"Unknown\"."
                            )
                        },
                        {
                            # Embed the image using base64
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        }
                    ]
                }
            ],
            "temperature": 0.3,
            "max_tokens": 1024
        }

        # Send request to the Groq API
        response = requests.post(self.api_url, headers=headers, json=prompt)

        # Successful response from API
        if response.status_code == 200:
            result: str = response.json()['choices'][0]['message']['content']
            name: str = self.extract_name(result)   # Extract name from structured answer
            return result, name

        # If request fails, return default "Unknown"
        return "Unknown", ""

    # ----------------------------------------------------------
    # Extract celebrity name from model output
    # ----------------------------------------------------------
    def extract_name(self, content: str) -> str:
        """
        Extract the celebrity name from the LLM's formatted output.

        Parameters
        ----------
        content : str
            Full textual response from the LLM.

        Returns
        -------
        str
            The extracted name, or "Unknown" if not found.
        """

        # Scan lines for the "Full Name" field
        for line in content.splitlines():
            if line.lower().startswith("- **full name**:"):
                return line.split(":", 1)[1].strip()

        return "Unknown"
