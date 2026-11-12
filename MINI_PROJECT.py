
import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("1000x550")
root.config(bg="#EAF2F8")
root.resizable(False, False)

# Quiz questions
questions = [
    {
        "question": "1. Who developed Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum",
                    "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "2. Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },
    {
        "question": "3. Which of the following is a Python data type?",
        "options": ["int", "float", "str", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "4. Which function is used to display output?",
        "options": ["input()", "display()", "print()", "show()"],
        "answer": "print()"
    },
    {
        "question": "5. Which keyword is used to define a function?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "6. Which collection stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "question": "7. Which operator is used for exponentiation?",
        "options": ["^", "**", "//", "%"],
        "answer": "**"
    },
    {
        "question": "8. Which keyword is used for a loop?",
        "options": ["repeat", "loop", "for", "iterate"],
        "answer": "for"
    },
    {
        "question": "9. Which method adds an element to a list?",
        "options": ["add()", "append()", "insertEnd()", "push()"],
        "answer": "append()"
    },
    {
        "question": "10. Which extension is used for Python files?",
        "options": [".java", ".cpp", ".py", ".html"],
        "answer": ".py"
    }
]

# Variables
current_question = 0
score = 0
selected_answer = tk.StringVar()

# Heading
heading = tk.Label(
    root,
    text="QUIZ APPLICATION",
    font=("Arial", 20, "bold"),
    bg="#EAF2F8",
    fg="#154360"
)
heading.pack(pady=20)

# Progress label
progress_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#EAF2F8"
)
progress_label.pack(pady=5)

# Question label
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#EAF2F8",
    wraplength=520
)
question_label.pack(pady=20)

# Options frame
options_frame = tk.Frame(root, bg="#EAF2F8")
options_frame.pack()

# Radio buttons
radio_buttons = []

for i in range(4):
    radio = tk.Radiobutton(
        options_frame,
        text="",
        variable=selected_answer,
        value="",
        font=("Arial", 12),
        bg="#EAF2F8",
        anchor="w",
        width=35
    )
    radio.pack(anchor="w", pady=5)
    radio_buttons.append(radio)

# Display question
def load_question():

    selected_answer.set("")

    if current_question < len(questions):

        question = questions[current_question]

        progress_label.config(
            text=f"Question {current_question + 1} of {len(questions)}"
        )

        question_label.config(text=question["question"])

        for i in range(4):
            radio_buttons[i].config(
                text=question["options"][i],
                value=question["options"][i]
            )

        next_button.config(text="Next Question")

    else:
        show_result()


# Check answer and move to next question
def next_question():

    global current_question, score

    if selected_answer.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please select an answer!"
        )
        return

    correct_answer = questions[current_question]["answer"]

    if selected_answer.get() == correct_answer:
        score += 1

    current_question += 1

    load_question()


# Display final result
def show_result():

    question_label.config(
        text=f"Quiz Completed!\n\nYour Score: {score}/{len(questions)}"
    )

    progress_label.config(text="Congratulations!")

    options_frame.pack_forget()
    next_button.pack_forget()

    percentage = (score / len(questions)) * 100

    result_label.config(
        text=f"Percentage: {percentage:.1f}%"
    )

    restart_button.pack(pady=20)


# Restart quiz
def restart_quiz():

    global current_question, score

    current_question = 0
    score = 0

    restart_button.pack_forget()
    options_frame.pack()
    next_button.pack(pady=20)

    result_label.config(text="")

    load_question()


# Next button
next_button = tk.Button(
    root,
    text="Next Question",
    font=("Arial", 12, "bold"),
    bg="#2874A6",
    fg="white",
    command=next_question,
    width=18
)
next_button.pack(pady=20)

# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#EAF2F8",
    fg="#117A65"
)
result_label.pack()

# Restart button
restart_button = tk.Button(
    root,
    text="Restart Quiz",
    font=("Arial", 12, "bold"),
    bg="#239B56",
    fg="white",
    command=restart_quiz,
    width=18
)

# Load first question
load_question()

# Run application
root.mainloop()
