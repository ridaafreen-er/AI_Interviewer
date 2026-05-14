from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import random

app = Flask(__name__)

print("AI Interviewer app is starting...")

# Interview Question Bank
QUESTIONS = ["Why do you want to work for our company?",
	"Where do you see yourself in 5 years?",
	"How do you handle stress or pressure?",
	"What motivates you?",
	"Are you a team player or do you prefer working alone?",
	"Do you have any questions for us?",
    "Tell me about yourself.",
    "What are your strengths?",
    "What is your biggest weakness?",
    "Why should we hire you?",
    "Describe a challenging situation you handled."
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "How many technical projects do you have in your portfolio?",
        "options": [
            {"text": "0", "score": 0},
            {"text": "1-2", "score": 10},
            {"text": "3-5", "score": 20},
            {"text": "5+", "score": 25}
        ]
    },
    {
        "id": 2,
        "question": "What is the status of your resume?",
        "options": [
            {"text": "Not started", "score": 0},
            {"text": "In progress", "score": 10},
            {"text": "Completed & reviewed", "score": 25}
        ]
    },
    {
        "id": 3,
        "question": "How confident are you with technical coding questions?",
        "options": [
            {"text": "Not confident", "score": 5},
            {"text": "Somewhat confident", "score": 15},
            {"text": "Very confident", "score": 25}
        ]
    },
    {
        "id": 4,
        "question": "How would you rate your communication skills?",
        "options": [
            {"text": "Need improvement", "score": 5},
            {"text": "Good", "score": 15},
            {"text": "Excellent", "score": 25}
        ]
    },
    {
        "id": 5,
        "question": "How many mock interviews have you practiced?",
        "options": [
            {"text": "None", "score": 0},
            {"text": "1-2", "score": 15},
            {"text": "5+", "score": 25}
        ]
    },
    {
        "id": 6,
        "question": "Do you have a live portfolio or GitHub link ready?",
        "options": [
            {"text": "No", "score": 0},
            {"text": "Yes, but needs work", "score": 10},
            {"text": "Yes, it's polished", "score": 25}
        ]
    }
]

TECHNICAL_QUESTIONS = {
    "web": [
        {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyperlink and Text Markup Language"], "answer": 0},
        {"question": "Which CSS property is used to change the background color?", "options": ["color", "background-color", "bgcolor"], "answer": 1},
        {"question": "What is the purpose of 'use strict' in JavaScript?", "options": ["Forces strict variable naming", "Enables strict mode for better error handling", "Prevents use of global variables"], "answer": 1}
    ],
    "backend": [
        {"question": "What is the primary purpose of a database index?", "options": ["To encrypt data", "To speed up data retrieval", "To reduce storage space"], "answer": 1},
        {"question": "Which HTTP method is most appropriate for creating a new resource?", "options": ["GET", "PUT", "POST"], "answer": 2},
        {"question": "What does ACID stand for in database transactions?", "options": ["Atomicity, Consistency, Isolation, Durability", "Accuracy, Complexity, Integrity, Design", "Access, Control, Identification, Distribution"], "answer": 0}
    ],
    "api": [
        {"question": "What does REST stand for?", "options": ["Representational State Transfer", "Remote Extension Service Tool", "Resource Exchange Standard Template"], "answer": 0},
        {"question": "Which HTTP status code represents a successful resource creation?", "options": ["200 OK", "201 Created", "204 No Content"], "answer": 1},
        {"question": "What is the main format used in modern Web APIs?", "options": ["XML", "CSV", "JSON"], "answer": 2}
    ],
    "ai_ds_ml": [
        {"question": "What is Supervised Learning?", "options": ["Learning without labeled data", "Learning with labeled data", "Learning through trial and error"], "answer": 1},
        {"question": "Which Python library is primarily used for data manipulation (DataFrames)?", "options": ["NumPy", "Pandas", "Scikit-Learn"], "answer": 1},
        {"question": "In a neural network, what is the purpose of an activation function?", "options": ["To initialize weights", "To introduce non-linearity", "To normalize input data"], "answer": 1}
    ]
}

FILLER_WORDS = ["um", "uh", "like", "actually", "basically", "you know"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz_page():
    return render_template("quiz.html")

@app.route("/portfolio_page")
def portfolio_page():
    return render_template("portfolio.html")

@app.route("/technical-questions/<topic>")
def get_technical_questions(topic):
    questions = TECHNICAL_QUESTIONS.get(topic, [])
    return jsonify(questions)

@app.route("/submit-technical-quiz", methods=["POST"])
def submit_technical_quiz():
    data = request.get_json()
    user_answers = data.get("answers", [])
    topic = data.get("topic")
    
    questions = TECHNICAL_QUESTIONS.get(topic, [])
    correct_count = 0
    
    for i, ans in enumerate(user_answers):
        if i < len(questions) and ans == questions[i]["answer"]:
            correct_count += 1
            
    score = int((correct_count / len(questions)) * 100) if questions else 0
    
    level = "Beginner"
    if score >= 80: level = "Advanced"
    elif score >= 50: level = "Intermediate"
    
    return jsonify({
        "score": score,
        "level": level,
        "correct": correct_count,
        "total": len(questions)
    })

@app.route("/quiz-questions")
def get_quiz_questions():
    return jsonify(QUIZ_QUESTIONS)

@app.route("/submit-quiz", methods=["POST"])
def submit_quiz():
    data = request.get_json()
    answers = data.get("answers", [])
    
    total_score = sum(answers)
    max_possible = len(QUIZ_QUESTIONS) * 25 
    percentage = (total_score / max_possible) * 100
    
    level = "Beginner"
    if percentage >= 80:
        level = "Ready"
    elif percentage >= 50:
        level = "Intermediate"
        
    tips = []
    if percentage < 80:
        tips.append("Consider building more projects for your portfolio.")
    if percentage < 60:
        tips.append("Focus on improving your technical fundamentals.")
    if percentage < 40:
        tips.append("Refine your resume and practice basic communication.")
        
    return jsonify({
        "score": int(percentage),
        "level": level,
        "tips": tips
    })

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

TECHNICAL_SKILLS = ["python", "javascript", "html", "css", "sql", "git", "react", "node", "flask", "django", "aws", "docker", "kubernetes", "java", "c++", "ruby", "php", "typescript", "mongodb", "postgresql"]
IMPACT_WORDS = ["developed", "implemented", "designed", "managed", "led", "optimized", "increased", "reduced", "solved", "created", "built", "delivered"]

@app.route("/analyze-portfolio", methods=["POST"])
def analyze_portfolio():
    data = request.get_json()
    text = data.get("portfolio_text", "").lower()
    
    if not text.strip():
        return jsonify({"error": "Please provide some text to analyze."}), 400

    words = text.split()
    
    # 1. Skill Analysis
    found_skills = [s for s in TECHNICAL_SKILLS if s in text]
    skill_score = min(10, len(found_skills) * 2)
    
    # 2. Impact Analysis
    found_impacts = [w for w in IMPACT_WORDS if w in text]
    impact_score = min(10, len(found_impacts) * 1.5)
    
    # 3. Tone Analysis
    sentiment = TextBlob(text).sentiment.polarity
    tone_score = max(1, min(10, int((sentiment + 1) * 5)))
    
    # 4. Overall Score
    overall_score = int((skill_score + impact_score + tone_score) / 3 * 10)
    
    feedback = []
    if len(found_skills) < 3:
        feedback.append("Try to highlight more specific technical skills.")
    if len(found_impacts) < 3:
        feedback.append("Use more action verbs like 'Optimized' or 'Delivered' to show impact.")
    if tone_score < 5:
        feedback.append("Your tone seems a bit passive. Try using more assertive and positive language.")
    if len(words) < 50:
        feedback.append("Your portfolio description is a bit short. Add more details about your projects.")

    return jsonify({
        "score": overall_score,
        "skills": found_skills,
        "impacts": found_impacts,
        "tone": tone_score,
        "feedback": feedback
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port) 
