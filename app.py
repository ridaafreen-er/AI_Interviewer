from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import random

app = Flask(__name__)

# Interview Question Bank
QUESTIONS = ["Why do you want to work for our company?",
	"Where do you see yourself in 5 years?",
	"How do you handle stress or pressure?",
	"What motivates you?",
	"Are you a team player or do you prefer working alone?",
	"Do you have any questions for us?"  
    "Tell me about yourself.",
    "What are your strengths?",
    "What is your biggest weakness?",
    "Why should we hire you?",
    "Describe a challenging situation you handled."
]

FILLER_WORDS = ["um", "uh", "like", "actually", "basically", "you know"]

@app.route("/")
def home():
    return render_template("index.html")

# Send random interview question
@app.route("/question")
def get_question():
    return jsonify({
        "question": random.choice(QUESTIONS)
    })

# Analyze answer
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    answer = data.get("answer", "").lower()

    words = answer.split()
    filler_count = sum(words.count(w) for w in FILLER_WORDS)

    sentiment = TextBlob(answer).sentiment.polarity
    confidence = max(1, min(10, int((sentiment + 1) * 5)))
    clarity = max(1, 10 - filler_count)

    feedback = []

    if filler_count > 3:
        feedback.append("Reduce filler words to sound more confident.")

    if confidence < 5:
        feedback.append("Use more positive and assertive language.")

    if len(words) < 20:
        feedback.append("Answer is too short. Try adding examples or details.")

    return jsonify({
        "confidence": confidence,
        "clarity": clarity,
        "filler_words": filler_count,
        "feedback": feedback
    })

if __name__ == "__main__":
    app.run(debug=True) 