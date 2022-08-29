from cgitb import text
from tkinter import Button, Canvas, Label, PhotoImage, Tk, font
from turtle import xcor, ycor
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Questions",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        thick_image = PhotoImage(file="images/true.png")
        cross_image = PhotoImage(file="images/false.png")
        self.thick_button = Button(
            image=thick_image, highlightthickness=0, command=self.thick_button_clicked)
        self.cross_button = Button(
            image=cross_image, highlightthickness=0, command=self.cross_button_clicked)
        self.cross_button.grid(row=2, column=1)
        self.thick_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text=f"You've completed the quiz. Your score is {self.quiz.score}/10")
            self.cross_button.config(state="disabled")
            self.thick_button.config(state="disabled")

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
        self.btn_delay()

    def thick_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def cross_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def enable_buttons(self):
        self.cross_button.config(state="normal")
        self.thick_button.config(state="normal")

    def btn_delay(self):

        self.cross_button.config(state="disabled")
        self.thick_button.config(state="disabled")
        self.cross_button.after(1000, self.enable_buttons)
        self.thick_button.after(1000, self.enable_buttons)
