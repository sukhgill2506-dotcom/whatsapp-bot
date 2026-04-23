from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "mytoken123"

# Home route (just to check if server is running)
@app.route("/", methods=["GET"])
def home():
    return "Bot is running", 200

# Webhook route (IMPORTANT)
@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # Step 1: Verification (GET request from Meta)
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403

    # Step 2: Receive messages (POST request from WhatsApp)
    if request.method == "POST":
        data = request.get_json()
        print("Incoming webhook:", data)
        return "EVENT_RECEIVED", 200


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
