from tkinter import *

root = Tk()
root.title("Justin Winchester's Metric Conversion App")


frame1 = Frame(root)
frame1.pack()

titleLabel = Label(frame1, text="Justin Winchester's Metric Conversion Application!", font="georgia", fg="red")
titleLabel.pack(pady=28)

#Make and pack widgets for input of miles and it's output in kilometers

frame2 = Frame(root)
frame2.pack()

inputMilesLabel = Label(frame2, text="Miles: ")
inputMilesLabel.pack(side=LEFT, pady=5)

userEntryMiles = Entry(frame2, bd=4)
userEntryMiles.pack(side=RIGHT)

frame3 = Frame(root)
frame3.pack()

outputLabelMiles = Label(frame3, text="Kilometers: ")
outputLabelMiles.pack(side=LEFT, pady=5)

resultStringMiles = StringVar()
resultLabelMiles = Label(frame3, textvariable=resultStringMiles)
resultLabelMiles.pack(side=RIGHT)

frame4 = Frame(root)
frame4.pack()

inputPoundsLabel = Label(frame4, text="Pounds: ")
inputPoundsLabel.pack(side=LEFT,pady=5)

userEntryPounds = Entry(frame4, bd=4)
userEntryPounds.pack(side=RIGHT)

frame5 = Frame(root)
frame5.pack()

outputLabelMiles = Label(frame5, text="Kilograms: ")
outputLabelMiles.pack(side=LEFT,pady=5)

resultStringPounds = StringVar()
resultLabelPounds = Label(frame5, textvariable=resultStringPounds)
resultLabelPounds.pack(side=RIGHT)



def CalculateMiles():
    userInput = userEntryMiles.get()
    num = float(userInput)
    kilometers = (num * 1.60934)
    resultStringMiles.set(str(kilometers))


def CalculatePounds():
    userInput2 = userEntryPounds.get()
    num2 = float(userInput2)
    kilograms = (num2 / 2.205)
    resultStringPounds.set(str(kilograms))


def Quit():
    root.destroy()


convertLengthButton = Button(root, text="Convert Length", relief=RAISED, bd=7, command=CalculateMiles)
convertLengthButton.pack(side=LEFT, ipadx=20)

convertLengthButton = Button(root, text="Convert Mass", relief=RAISED, bd=7, command=CalculatePounds)
convertLengthButton.pack(side=LEFT, ipadx=20)

quitButton = Button(root, text="Quit", relief=RAISED, bd=7, command=Quit)
quitButton.pack(side=RIGHT, ipadx=15)


root.mainloop()