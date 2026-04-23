from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running 🚀"

@app.route("/webhook")
def webhook():
    return "Webhook working ✅"

if __name__ == "__main__":
    app.run()
