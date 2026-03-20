import openai
from ttkthemes import ThemedTk
from tkinter import ttk

client = openai.OpenAI(api_key = "YOUR_API_KEY_HERE")

window = ThemedTk(theme="breeze")
window.configure(themebg="breeze")
window.geometry("600x600")
window.title("GPT-GeographyQuiz")
window.resizable(False, False)

score = 0
questions = 0
MAX_QUESTIONS = 5
prev_questions = set()

def check(guess):
    global score, questions

    if questions >= MAX_QUESTIONS:
        return

    questions += 1
    progress_bar["value"] = questions

    if answer == guess:
        score += 1

        lbl_score.configure(text=f"Score: {score}/{questions}")

    if questions == MAX_QUESTIONS:
        end_game()
    else:
        generate_question()

def end_game():
    for widget in window.winfo_children():
        widget.destroy()

    end_lbl = ttk.Label(window, text="THE END", font=("Arial", 60, "bold"), foreground="red")
    end_lbl.pack(pady=20)

    score_lbl = ttk.Label(window, text=f"Score: {score}/{questions}", font=("Arial", 30, "bold"))
    score_lbl.pack(pady=10)

    reset_btn = ttk.Button(window, text="Play Again", command=reset_game)
    reset_btn.pack(pady=20)

question_label = ttk.Label(window, text="", font=20)
question_label.pack(pady=15)

frame = ttk.Frame(window)
frame.pack()

yes_btn = ttk.Button(frame, text="Yes", command = lambda : check("yes"))
yes_btn.pack(side="left")
no_btn = ttk.Button(frame, text="No", command = lambda : check("no"))
no_btn.pack()

lbl_score = ttk.Label(window, text="", font=20)
lbl_score.pack()

progress_bar = ttk.Progressbar(window, orient="horizontal", length=400)
progress_bar["maximum"] = MAX_QUESTIONS
progress_bar.pack()

def reset_game():
    global score, questions, prev_questions
    score = 0
    questions = 0
    prev_questions.clear()

    for widget in window.winfo_children():
        widget.destroy()

    global question_label, frame, yes_btn, no_btn, lbl_score, progress_bar

    question_label = ttk.Label(window, text="", font=20)
    question_label.pack(pady=15)

    frame = ttk.Frame(window)
    frame.pack()

    yes_btn = ttk.Button(frame, text="Yes", command=lambda: check("yes"))
    yes_btn.pack(side="left")

    no_btn = ttk.Button(frame, text="No", command=lambda: check("no"))
    no_btn.pack()

    lbl_score = ttk.Label(window, text="", font=20)
    lbl_score.pack()

    progress_bar = ttk.Progressbar(window, orient="horizontal", length=400)
    progress_bar.pack()

    generate_question()


def generate_question():
    global answer, question

    for _ in range(MAX_QUESTIONS):
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": "Generate an insanely hard yes/no question in English about geography for professionals with a clear correct answer. Do not say anything more than the question and the answer. Return the format: 'Question: <question> | Answer: <yes/no>'"
                },
                {"role": "user", "content": "Generate a simple yes/no question."}
            ]
        )

        result = response.choices[0].message.content.strip()
        question_part, answer_part = result.split(" | ")

        if question_part not in prev_questions:
            prev_questions.add(question_part)

            question = question_part.replace("Question: ", "").strip()
            answer = answer_part.replace("Answer: ", "").lower().strip()

            question_label.configure(text=question)
            return
generate_question()

window.mainloop()
