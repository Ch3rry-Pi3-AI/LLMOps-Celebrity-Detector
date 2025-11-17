# 🐳 **Containerisation & Kubernetes Deployment — LLMOps Celebrity Detector**

This branch introduces **containerisation** and **Kubernetes deployment** for the LLMOps Celebrity Detector.
With this stage complete, the application can now run inside a Docker container and be deployed reliably on any Kubernetes cluster.

Two new files are added:

* A `Dockerfile` that packages the full Flask app
* A Kubernetes manifest (`kubernetes-deployment.yaml`) that deploys and exposes the container

## 🗂️ **Project Structure (Updated)**

Only the **new files** added in this branch are annotated.

```text
LLMOPS-CELEBRITY-DETECTOR/
├── .circleci/
├── .venv/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── utils/
│       ├── __init__.py
│       ├── image_handler.py
│       ├── celebrity_detector.py
│       └── qa_engine.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── Dockerfile                        # NEW: Builds the production container image
├── kubernetes-deployment.yaml        # NEW: Kubernetes Deployment + Service manifest
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

## 🧱 **Dockerfile — Container Build Instructions**

The `Dockerfile` defines everything required to run the Flask application inside a container:

* Uses a stable Python base image
* Installs all dependencies
* Copies the entire project structure
* Exposes port `5000`
* Sets the main entrypoint (`python app.py`)

Once built, the resulting image can run on:

* Your local machine
* Docker Desktop
* Any cloud provider
* Any Kubernetes cluster

Build the image locally:

```bash
docker build -t llmops-celebrity-detector .
```

Run it:

```bash
docker run -p 5000:5000 llmops-celebrity-detector
```

## ☸️ **kubernetes-deployment.yaml — Cluster Deployment**

This manifest contains **two Kubernetes resources**:

* A **Deployment** that runs the container inside the cluster
* A **LoadBalancer Service** that exposes the app externally

The `---` between the resources is required because Kubernetes treats them as separate documents.

Apply it to your cluster:

```bash
kubectl apply -f kubernetes-deployment.yaml
```

Check that it deployed correctly:

```bash
kubectl get pods
kubectl get svc
```

Once the LoadBalancer provisions an external IP, the app becomes available publicly.

## 🚀 **End-to-End Flow Enabled by This Branch**

With this branch complete, you can now:

1. Build a Docker image for the system
2. Push it to a registry (DockerHub, GCP Artifact Registry, etc.)
3. Deploy it to Kubernetes
4. Access the application from an external IP

This marks the transition from a **local development app** to a **cloud-deployable service**.

## ✅ **In Summary**

This branch adds the full deployment backbone for the LLMOps Celebrity Detector:

* A reproducible Docker image
* A Kubernetes manifest ready for production
* Simple deployment commands
* A clean separation between build (Dockerfile) and runtime orchestration (K8s)

Your app is now fully containerised and cloud-deployable.
