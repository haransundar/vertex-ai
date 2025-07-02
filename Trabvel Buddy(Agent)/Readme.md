# Travel Buddy Agent – A Vertex AI Conversational Assistant

![AI](https://img.shields.io/badge/AI-Generative-blue)
![Platform](https://img.shields.io/badge/Platform-Google%20Cloud%20Vertex%20AI-black)
![License](https://img.shields.io/badge/License-MIT-green)

**Travel Buddy Agent** is a conversational travel assistant built using **Google Cloud's Vertex AI Agent Builder**, integrated into a **Flask web application** and deployed via **Cloud Run**.

This project demonstrates how to create, ground, simulate, and embed an AI agent into a real-time web interface using minimal code — ideal for rapid prototyping of assistant experiences.



## ✨ Key Features

- **Conversational Agent Creation:** Built with Vertex AI Agent Builder and Dialogflow Messenger.
- **Flask Web Integration:** Embedded into a lightweight Flask app with a fully styled UI.
- **Grounded Responses:** Uses Datastore for accurate fallback suggestions (e.g., for unknown queries like “Wakanda”).
- **Deployed to Cloud Run:** Easily deployable using Docker and Cloud Build.
- **Custom Persona:** Helpful, knowledgeable, and travel-savvy AI that assists with planning, bookings, and queries.

---

## 🤖 The Problem It Solves

Planning trips can be time-consuming. This agent acts as an intelligent virtual travel assistant, helping users with:
- Exploring destinations  
- Checking visa or travel requirements  
- Recommending similar places if data is unavailable  
- Simulating helpful interaction on the web

---

## 🛠️ Technology Stack

- **AI Framework:** Google Cloud Vertex AI Agent Builder (Dialogflow interface)
- **Frontend Integration:** Dialogflow Messenger Web SDK
- **Web Server:** Python Flask
- **Deployment:** Google Cloud Run (containerized via Docker)
- **Assistive Tooling:** Gemini Code Assist for auto-generating app scaffolding

---

## 💡 The Use Case Vision

This project acts as a foundational template for:
- Domain-specific travel planners
- Hotel or airline customer service bots
- Local tourism board assistants
- Hobbyist AI web agents using minimal backend logic

---

## ⚙️ How It Works

1. **Create the agent** in Vertex AI Agent Builder.
2. **Ground it with Datastore**, enabling accurate responses for unknown queries.
3. **Embed the agent** into an HTML page using the Dialogflow Messenger snippet.
4. **Serve via Flask** and deploy to Cloud Run using Docker.

---

## 📁 Project Structure
```bash
vertex-ai/
└── travel-buddy-agent/
├── app.py # Flask backend
└── templates/
└── index.html # HTML + Dialogflow Messenger
```

---

## 🚀 Deployment Guide

**Run Locally**
```bash
pip install flask
python app.py
Visit: http://localhost:5000

Deploy to Google Cloud Run

Create Dockerfile

Build the image:

bash
Copy
Edit
gcloud builds submit --tag gcr.io/<project-id>/travel-buddy
Deploy:

bash
Copy
Edit
gcloud run deploy travel-buddy \
  --image gcr.io/<project-id>/travel-buddy \
  --region us-central1 \
  --allow-unauthenticated

```
---

## 📦 Extending the Agent
Want to reuse this project for a different conversational AI use case? You can easily extend it by following these steps:

Create a New Agent
Use the Vertex AI Agent Builder to create a new agent tailored to your domain (e.g., healthcare, real estate, education).

Update the Frontend
Open templates/index.html and replace the following attributes in the <df-messenger> tag:

html
Copy
Edit
<df-messenger
  project-id="your-new-project-id"
  agent-id="your-new-agent-id"
  ...
>
Restart Your Flask App

bash
Copy
Edit
python app.py
Your new AI agent will now be live on the same web interface.

✅ Tip: Each agent can have a distinct persona and goal, allowing you to build a full suite of specialized AI assistants.

## 🧾 License
This project is licensed under the MIT License.
See the LICENSE file for full details. You are free to use, modify, and distribute this project in both personal and commercial contexts, as long as the original license is retained.
