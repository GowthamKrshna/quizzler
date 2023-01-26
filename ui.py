from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score:', fg='white', bg=THEME_COLOR)
        self.score.grid(column=2, row=0)

        self.canvas = Canvas(width=300, height=260, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     130,
                                                     text='Some Question',
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic')
                                                     )
        self.canvas.grid(column=1, row=1, columnspan=2, pady=30)

        right = PhotoImage(file='images/true.png')
        self.right_btn = Button(image=right, highlightthickness=0, command=self.check_right)
        self.right_btn.grid(column=1, row=2)
        wrong = PhotoImage(file='images/false.png')
        self.wrong_btn = Button(image=wrong, highlightthickness=0, command=self.check_wrong)
        self.wrong_btn.grid(column=2, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score:{self.quiz.score}')
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.wrong_btn.config(state='disabled')
            self.right_btn.config(state='disabled')

    def check_right(self):
        is_right= self.quiz.check_answer('True')
        self.give_feedback(is_right)
    def check_wrong(self):
        is_right= self.quiz.check_answer('False')
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

