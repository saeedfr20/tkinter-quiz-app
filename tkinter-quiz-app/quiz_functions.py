import json
from tkinter import messagebox

def getQuestions():
    try:
        with open('quest.json') as f:
            q = json.load(f)
        return q
    except FileNotFoundError:
        messagebox.showinfo(message="Error: Questions file not found! Please make sure 'quest.json' exists.")
        return {}
    except json.JSONDecodeError:
        messagebox.showinfo(message="Error: Invalid or empty JSON in 'quest.json'.")
        return {}

idx = 0
score = 0
def nextAction(txtAnswer,lblQuestion,btnNext,lblMsg,answer,questions):
    global idx, score
    currentAnswer = txtAnswer.get()
    if currentAnswer == '':
        messagebox.showinfo(message='Please enter your answer!')
        return
    if currentAnswer.lower() == answer[idx]:
        messagebox.showinfo(message='correct!')
        score += 1
        lblMsg.configure(text=f'Your Score:{score}')
    else:
        messagebox.showinfo(message='not correct!')
    idx += 1
    if idx >= len(questions):
        lblQuestion.configure(text="Finished", font=("Helvetica ", 16), fg="Red")
        btnNext.configure(state='disabled')
    else:
        lblQuestion.configure(text=questions[idx])
    txtAnswer.delete(0, 'end')