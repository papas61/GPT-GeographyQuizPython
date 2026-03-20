# 🌍 GPT Geography Quiz

A desktop quiz game built with Python and Tkinter that generates extremely difficult yes/no geography questions using the OpenAI API.

---

## 🎮 Features

* 🧠 AI-generated **professional-level geography questions**
* ✅ Yes / No gameplay
* 📊 Score tracking
* 📈 Progress bar (fills as you answer questions)
* 🔁 Replay functionality
* 🚫 No duplicate questions per session

---

## 🖥️ Preview

* Answer up to **5 questions**
* See your final score at the end
* Click **"Play Again"** to restart

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install openai ttkthemes
```

---

## 🔑 API Key

The app uses the OpenAI API.

Replace this line in the code:

```python
client = openai.OpenAI(api_key="YOUR_API_KEY_HERE")
```

with your own API key.

---

## ▶️ How to Run

```bash
python your_script_name.py
```

---

## 🧩 How It Works

* The app sends a request to the OpenAI model (`gpt-4.1`)
* It generates a **yes/no geography question**
* The app:

  * Parses the response
  * Avoids duplicates using a `set`
  * Updates score and progress bar
* After 5 questions, the game ends

---

## 📊 Game Logic

* Total questions: **5**
* Progress bar fills with each answer
* Score increases only on correct answers
* Final screen shows:

  * Score
  * Restart button

---

## ⚠️ Notes

* Make sure you have internet access (API required)
* Avoid sharing your API key publicly
* The model may occasionally repeat questions (handled in code)

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

Made with Python + OpenAI

<img width="600" height="628" alt="image" src="https://github.com/user-attachments/assets/54978c19-8325-4598-9c4c-4d4d12eb4f4c" />
