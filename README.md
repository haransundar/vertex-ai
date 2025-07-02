```markdown
# Travel Buddy Agent

A conversational AI “Travel Buddy” built with Google Cloud’s Vertex AI Agent Builder, Dialogflow Messenger, and Flask.

---

## 📂 Project Structure

```

travel-buddy-agent/
├── app.py            # Flask application integrating your Dialogflow Messenger snippet
└── templates/
└── index.html    # HTML template with embedded Dialogflow Messenger UI

````

---

## 🚀 Quick Start

1. **Clone & enter the project**  
   ```bash
   git clone https://github.com/<your-username>/vertex-ai.git
   cd vertex-ai/travel-buddy-agent
````

2. **Install dependencies**
   Ensure you have Python 3 and pip installed, then:

   ```bash
   pip install flask
   ```

3. **(Optional) Configure environment variables**
   If you prefer not to hard‑code your agent IDs in `index.html`, set:

   ```bash
   export DIALOGFLOW_PROJECT_ID=<your-project-id>
   export DIALOGFLOW_AGENT_ID=<your-agent-id>
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

   By default it will listen on `http://localhost:5000`.

5. **Open in browser**
   Visit `http://localhost:5000` to start chatting with **Travel Buddy**.

---

## 🛠️ Implementation Details

* **app.py**

  * Serves a single route (`/`) that renders `templates/index.html`.
  * No additional backend logic—Dialogflow Messenger handles all conversational flows.

* **templates/index.html**

  * Loads the Dialogflow Messenger CSS & JS.
  * Embeds the `<df-messenger>` tag with your Vertex AI Agent’s `project-id` and `agent-id`.
  * Applies custom CSS properties (colors, positioning) to match your site’s look & feel.

---

## 📦 Adding New Agents

To demo another Vertex AI agent in this same folder:

1. Update `templates/index.html`:

   * Change the `<df-messenger project-id="…" agent-id="…">` attributes.
2. (If needed) tweak styling or add new HTML around the `<df-messenger>` tag.
3. Restart the Flask app—your new agent will appear in the same UI.

---

## 🚢 Deployment

You can containerize and deploy this app to Google Cloud Run:

1. **Create a `Dockerfile`** (example):

   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY . /app
   RUN pip install flask
   EXPOSE 5000
   CMD ["python", "app.py"]
   ```
2. **Build & push**

   ```bash
   gcloud builds submit --tag gcr.io/<your-project-id>/travel-buddy
   ```
3. **Deploy to Cloud Run**

   ```bash
   gcloud run deploy travel-buddy \
     --image gcr.io/<your-project-id>/travel-buddy \
     --region us-central1 \
     --allow-unauthenticated
   ```

---

## 🤝 Contributing & License

Feel free to open issues or pull requests!
This project is licensed under the MIT License. See [LICENSE](../LICENSE) in the root repo for details.

```
```
