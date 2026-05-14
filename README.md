# AI Interviewer 🚀

AI Interviewer is a comprehensive, professional platform designed to help job seekers prepare for interviews using AI-driven feedback, technical quizzes, and portfolio analysis.

![Status](https://img.shields.io/badge/Status-Deployed-success)
![Platform](https://img.shields.io/badge/Platform-Render-blue)
![Tech](https://img.shields.io/badge/Tech-Flask%20%7C%20Python%20%7C%20Glassmorphism-brightgreen)

## ✨ Features

### 1. **Interactive AI Interview**
- **Dynamic Chat**: Practice real-world interview questions.
- **Sentiment Analysis**: Get feedback on your tone and confidence using `TextBlob`.
- **Filler Word Detection**: The AI tracks filler words (um, uh, like) to help you sound more professional.

### 2. **Technical Quiz Suite**
- **Topic-Specific MCQs**: Test your knowledge in Web Dev, Backend, API, and AI/DS/ML.
- **Readiness Scoring**: Get an instant percentage score and level assessment (Beginner, Intermediate, Ready).

### 3. **Portfolio Intelligence Report**
- **Smart Scanning**: Analyzes your projects for 20+ technical skills.
- **Impact Analysis**: Detects professional action verbs to measure the "velocity" of your experience.
- **Strategic Feedback**: Receive AI-generated tips on how to strengthen your profile.

### 4. **Modern Glassmorphic UI**
- **Sleek Design**: High-end translucent navigation and components.
- **Responsive**: Fully optimized for both desktop and mobile viewing.

---

## 🛠️ Tech Stack

- **Backend**: Python (Flask)
- **AI/NLP**: TextBlob (Sentiment & Language Analysis)
- **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript (Vanilla)
- **Server**: Gunicorn (Production Grade)
- **Deployment**: Render

---

## 🚀 Quick Start

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ridaafreen-er/AI_Interviewer.git
   cd AI_Interviewer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```
   *The app will be available at `http://localhost:8080`*

### Deployment

This project is ready for deployment on **Render**, **Heroku**, or **AWS**.

1. Connect your GitHub repo to your hosting provider.
2. Set **Build Command**: `pip install -r requirements.txt`
3. Set **Start Command**: `gunicorn app:app`
4. The app uses the `PORT` environment variable automatically.

---

## 📂 Project Structure

- `app.py`: Main Flask backend and AI logic.
- `templates/`: HTML5 templates (Index, Quiz, Portfolio).
- `static/`: CSS styling and images.
- `Procfile`: Configuration for production deployment.
- `requirements.txt`: Python dependencies.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
*Created by [Rida Aafreen](https://github.com/ridaafreen-er)*
