#Justin Winchester
#Program 4 Python GUI Summer 2021
#July 22, 2021
#This program is a general flash card application that has been enchanced to be a language learning practice application. This program uses a set list of words and phrases in German
#& Their corresponding translations in English. The purpose of the program is to assist the user with learning and practicing Basic phrases in the German Language and their English language counterparts.
#This program his been written using Tkinter Pyhton's GUI library and makes appropriate use of components such as widgets to accomplish this task. This program has a menu that allows the user to select
#An introductory informatory program message, a module to practice value pairs of German / English Words or phrases, and also a quiz which allows the user to enter the correct English translation of The
#German Words and phrases as they are randomly shuffled and placed on the screen via the duration of the program.

from tkinter import *
from random import randint


root = Tk()
root.title('Justin Winchester - German Language Learning App')
root.iconbitmap('c:/Users/justi/OneDrive/Desktop')
root.geometry("700x700")

def quiz():
    hide_all_frame()
    quiz_frame.pack(fill="both", expand=1)
    next()


def practice():
    hide_all_frame()
    practice_frame.pack(fill="both", expand=1)
    my_label4 = Label(practice_frame, text="German/ English Word Practice", font="georgia", fg="gold", bg="green" ).pack()
    practiceNext()


#Hide all previous frames
def hide_all_frame():
    messg_frame.pack_forget()
    quiz_frame.pack_forget()
    practice_frame.pack_forget()


def messgFrame():
    hide_all_frame()
    messg_frame.pack(fill="both", expand=1)
    next()


#Create the Menu
app_menu = Menu(root)
root.config(menu=app_menu)

#Create Menu Item(s)
german_menu = Menu(app_menu)
app_menu.add_cascade(label="Learn German", menu=german_menu)
german_menu.add_command(label="Program Message", command=messgFrame)
german_menu.add_command(label="German Words Quiz", command=quiz)
german_menu.add_command(label="Practice", command=practice)
german_menu.add_separator()
german_menu.add_command(label="Exit", command=root.quit)

quiz_frame = Frame(root, width=700, height=700, bg="white")
practice_frame = Frame(root, width=700, height=700)
messg_frame = Frame(root, width=700, height=700, bg="white")

germanEnglishWord = [
    (("Ja"),("Yes")),
    (("Nein"),("No")),
    (("Danke"),("Thank you")),
    (("Bitte"),("Please")),
    (("Entschuldigen Sie"),("Excuse Me")),
    (("Es tut mir leid"),("I'm  sorry")),
    (("Wo"),("Where")),
    (("Wo ist die Toilette?"),("Where's the restroom?")),
    (("Guten Tag"),("Hello")),
    (("Guten Morgen"),("Good morning")),
    (("Guten Abend"),("Good evening")),
    (("Gute Nacht"),("Good night")),
    (("Auf Wiedersehen")),("Good bye"),
    (("Bis spater"),("See you later")),
    (("Prost!"),("Cheers!")),
    (("Jut"),("Good")),
    (("Montag"),("Monday")),
    (("Sprechen Sie Englisch"),("Do you speak English?"))
]


count = len(germanEnglishWord)

def next():
    global helper, hint_count
    #clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    #Reset/ Clear Hints from previous question, recieve hints for next question
    helper = ""
    hint_count = 0

    #Create random selection
    global random_word
    random_word = randint(0, count-1)
    #update label with German word
    german_word.config(text=germanEnglishWord[random_word][0])



def practiceNext():
   #Create random selection
    global random_word2
    random_word2 = randint(0, count-1)
    #update label with German word
    english_word.config(text=germanEnglishWord[random_word2][1])
    german_word2.config(text=germanEnglishWord[random_word2][0])


def answer():
    if my_entry.get().capitalize() == germanEnglishWord[random_word][1]:
        answer_label.config(fg="white", bg="green", text=f"Way to go! That's Right {germanEnglishWord[random_word][0]} is {germanEnglishWord[random_word][1]}")
    else:
        answer_label.config(fg="white", bg="red",text=f"Sorry! {germanEnglishWord[random_word][0]} does NOT mean {my_entry.get().capitalize()}")


#Helper to keep track of the Hints
helper =""
hint_count = 0

def getHint():
    global hint_count
    global helper

    if hint_count < len(germanEnglishWord[random_word][1]):
        helper = helper + germanEnglishWord[random_word][1][hint_count]
        hint_label.config(text=helper)
        hint_count +=1


def Quit():
    root.destroy()




german_word = Label(quiz_frame, text="", font=("Helvetica",36))
german_word.pack(pady=50)

answer_label = Label(quiz_frame, text="", font=("georgia",18))
answer_label.pack(pady=20)

my_entry = Entry(quiz_frame, relief=RAISED, bd=7, font=("Helvetica", 18))
my_entry.pack(pady=20)

#Create Buttons
button_frame = Frame(quiz_frame)
button_frame.pack(pady=20)

answer_button = Button(button_frame, relief=GROOVE, bd=7,text="Answer", command=answer, bg="white", font="arial", fg="green")
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, relief=GROOVE, fg="purple", bg="white", bd=7,text="Next", font="arial", command=next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, relief=RAISED, bd=5, bg="white", font="georgia", fg="gold", text="Hint", command=getHint)
hint_button.grid(row=0, column=2, padx=20)

quitButton1 = Button(button_frame, text="Quit", relief=RAISED, bd=5, bg="white", font="arial", fg="red", command=Quit)
quitButton1.grid(row=1, column=1, pady=5)


#create hint label
hint_label = Label(quiz_frame, text=" ", bg="black", fg="white", font=("georgia",20))
hint_label.pack(pady=20)

#run next function when program starts
#next()


german_word2 = Label(practice_frame, text="", font=("Georgia", 36))
german_word2.pack(pady=50)

english_word = Label(practice_frame, text="", font=("Georgia", 36))
english_word.pack(pady=50)

button_frame2 = Frame(practice_frame)
button_frame2.pack(pady=10)

next_button2 = Button(button_frame2, relief=RAISED, bd=3, text="Next Pair", fg="purple", bg="white", command=practiceNext)
next_button2.grid(row=0, column=1)

quitButton2 = Button(button_frame2, text="Quit", relief=RAISED, bd=3, command=Quit)
quitButton2.grid(row=0, column=2)


messg_var = StringVar()
programMessage = Message(messg_frame, textvariable=messg_var, relief=GROOVE, font=("Georgia",18))

messg_var.set("Hello! Interested in sharpening up your foreign language skills?? \n Then you've chosen the right application, in this language practice application we will be studying the wonderful German Language! Just select from the menu in order to select from the application options. You"
        "can either choose to study the German & English Words / Phrase Pairs and then choose to select the Language Quiz, Don't worry if you don't remember them all just use the 'hint' option to get helpful "
        "hints regarding the letters identify the phrase or word in German, good luck and Enjoy!!")
programMessage.pack()



root.mainloop()