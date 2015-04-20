from tkinter import *
from login import *
import gspread, random, time

gc = gspread.login(login['username'],login['password'])
sh = gc.open("Mysterabbit Questions")

questionsBackup = {'green':sh.worksheet("Green Practices and Biodiversity").get_all_values(),'energy':sh.worksheet("Energy").get_all_values(),'compost':sh.worksheet("Compost vs. Landfill").get_all_values(),'recycling':sh.worksheet("Recycl$
questions = questionsBackup

root = Tk()

global labels
labels = []

def q():
    category = random.choice(list(questions.keys()))
    question = random.choice(questions[category])
    while question[0]=='Question':
        category = random.choice(list(questions.keys()))
        question = random.choice(questions[category])
#    print(questions)
    bg = {'green':'green','energy':'yellow','compost':'black','recycling':'blue','climate':'white','wt':'purple'}
    root.configure(background=bg[category])
    global labels
    labels = [Label(root, text=question[0], fg = "orange", bg = bg[category], font = "Verdana 16 bold"),
        Label(root, text="A: "+question[1], fg = "red", font = "Verdana 16 bold"),
        Label(root, text="B: "+question[2], fg = "yellow", font = "Verdana 16 bold"),
        Label(root, text="C: "+question[3], fg = "green", font = "Verdana 16 bold"),
        Label(root, text="D: "+question[4], fg = "blue", font = "Verdana 16 bold")]
    for label in labels:
        label.pack()
    answer = input("Answer: ")
    questionLetterMap = {'a':1,'b':2,'c':3,'d':4}
    if answer.lower() == question[5].lower():
        correct = "CORRECT! "+ question[6]#print("CORRECT!",question[6])
    else:
        correct = 'Sorry, incorrect. The correct answer is %s, "%s".' % (question[5].upper(), question[questionLetterMap[question[5].lower()]])#print('Sorry, incorrect. The correct answer is %s, "%s".' % (question[5].upper(), question[que$
    global infoLabel
    infoLabel = Label(root, text=correct, fg = "green", bg = "black", font = "Verdana 16 bold")
    infoLabel.pack()
    root.after(1000,prepareForNext)

def prepareForNext():
    global infoLabel
    infoLabel.pack_forget()
    time.sleep(1)
    global labels
    for label in labels:
        label.pack_forget()
    q()

q()
root.mainloop()
