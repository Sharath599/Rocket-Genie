from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Simple chatbot logic
    if "course" in user_message.lower():
        reply = "We offer Live Classes, Video Courses, and E-books."
    elif "exam" in user_message.lower():
        reply = "We currently have 35 certification exams available."
    elif "price" in user_message.lower():
        reply = "Please check our pricing section for latest offers."
    else:
        reply = "Thank you for your message. Our team will contact you soon."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
