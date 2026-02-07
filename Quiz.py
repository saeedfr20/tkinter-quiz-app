import tkinter
from quiz_functions import *





# -----------------main------------------------------------------------
info = getQuestions()
if info == {}:
    exit()
questions = list(info.keys())
answer = list(info.values())

win = tkinter.Tk()
win.title('Quiz')
win.geometry('500x300')

lblQuestion = tkinter.Label(win, text='')
lblQuestion.pack(pady=5)

lblAnswer = tkinter.Label(win, text="your answer:", font=("Helvetica ", 20), fg="black", bg="light blue")
lblAnswer.pack(pady=5)
win.configure(bg="Tan")


txtAnswer = tkinter.Entry(win, width=30, highlightthickness=4, highlightcolor='black', font=("Helvetica ", 14))
txtAnswer.pack(pady=10)

btnNext = tkinter.Button(win, text='Next....', command=lambda :nextAction(txtAnswer,lblQuestion,btnNext,lblMsg,answer,questions), font=("Helvetica ", 16), fg="black", bg="Silver")
btnNext.pack(pady=10)

lblMsg = tkinter.Label(win, text='Your Score:0', font=("Helvetica ", 16), fg="black", bg="Teal")
lblMsg.pack()



lblQuestion.configure(text=questions[idx], font=("Helvetica ", 16), fg="black")

win.mainloop()
