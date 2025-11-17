# ======================================================================
# 🐍 Base Image
# ======================================================================
# Use the lightweight Python 3.12 slim image as the foundation.
# This keeps the container small while still supporting OpenCV and Flask.
FROM python:3.12-slim


# ======================================================================
# 🔧 Environment Variables
# ======================================================================
# PYTHONDONTWRITEBYTECODE:
#     Prevents Python from generating .pyc files inside the container.
#
# PYTHONUNBUFFERED:
#     Ensures real-time output (no buffering), important for logs.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


# ======================================================================
# 📁 Working Directory
# ======================================================================
# All project files will live in /app inside the container.
WORKDIR /app


# ======================================================================
# 📦 System Dependencies
# ======================================================================
# Install essential OS packages required for:
# - OpenCV
# - Image processing
# - General build tools
#
# After installation, clean apt cache to keep the image lean.
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*


# ======================================================================
# 📥 Copy Application Code
# ======================================================================
# Copies *all* project files from the host into the container.
COPY . .


# ======================================================================
# 📦 Install Python Dependencies
# ======================================================================
# Install the project in editable mode using setup.py.
# --no-cache-dir avoids unnecessary layer bloat.
RUN pip install --no-cache-dir -e .


# ======================================================================
# 🌐 Expose Flask Port
# ======================================================================
# Flask runs on port 5000 by default.
EXPOSE 5000


# ======================================================================
# 🚀 Application Entrypoint
# ======================================================================
# Runs the Flask application using the project's main entry file.
CMD ["python", "app.py"]
