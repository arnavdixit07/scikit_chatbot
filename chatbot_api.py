from flask import Flask, request, jsonify, render_template
from AI import predict_intent, responses  # Your existing AI logic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    intent = predict_intent(user_input)
    reply = responses.get(intent, "Sorry, I didn't understand that.")
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)






