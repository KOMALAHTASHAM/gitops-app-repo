from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="font-family: Arial; text-align: center; margin-top: 100px; background-color: #f0f4f8;">
        <h1 style="color: #1a73e8;">GitOps Pipeline - Live!</h1>
        <p style="font-size: 18px;">Deployed via Cloud Build + GKE</p>
        <p style="color: green; font-weight: bold;">Version 3.4</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
