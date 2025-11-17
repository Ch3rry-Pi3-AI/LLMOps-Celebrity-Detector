"""
qa_engine.py

Utility module providing a lightweight Q&A engine for asking
follow-up questions about a recognised celebrity using the Groq LLM API.

Classes
-------
QAEngine
    Handles querying the model with user questions about a celebrity.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
import os
import requests
from typing import Optional


# --------------------------------------------------------------
# Celebrity Q&A Engine
# --------------------------------------------------------------
class QAEngine:
    """
    A utility class for asking LLM-driven questions about celebrities.

    Methods
    -------
    ask_about_celebrity(name, question)
        Sends a natural language question to the LLM and returns the response.
    """

    def __init__(self) -> None:
        """Initialise API credentials and model configuration."""
        self.api_key: Optional[str] = os.getenv("GROQ_API_KEY")     # Load API key from environment
        self.api_url: str = "https://api.groq.com/openai/v1/chat/completions"
        self.model: str = "meta-llama/llama-4-maverick-17b-128e-instruct"

    # ----------------------------------------------------------
    # Ask questions about a celebrity
    # ----------------------------------------------------------
    def ask_about_celebrity(self, name: str, question: str) -> str:
        """
        Ask a question about a specific celebrity.

        Parameters
        ----------
        name : str
            The name of the celebrity to be queried.
        question : str
            The user's natural language question.

        Returns
        -------
        str
            The model’s response, or a fallback error message.
        """

        # Prepare request headers
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Construct the prompt for the model
        prompt: str = (
            f"You are an AI assistant that knows a lot about celebrities. "
            f"Answer questions about {name} concisely and accurately.\n\n"
            f"Question: {question}"
        )

        # Define the payload for the API request
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.5,
            "max_tokens": 512
        }

        # Send the request to the Groq API
        response = requests.post(self.api_url, headers=headers, json=payload)

        # If successful, return text answer
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']

        # Fallback response for failed requests
        return "Sorry, I couldn't find the answer."
