from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page with the Vertex AI agent."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)