from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look I clicked a button!")
    myLabel.pack()

def tempConversionTableFC():
    print("TEMPERATURE \nConversion \nF   C\n_______")
    for tempInFahrenheit in range(80,100,2):
        tempInCelsius = round(5/9 * (tempInFahrenheit - 32))
        print(tempInFahrenheit, "\t", tempInCelsius)

def closeWindow():
    return root.destroy()

myCanvas = Canvas(root, bg = "skyblue", height = 50, width = 150)

oval = myCanvas.create_oval(50, 5, 100, 50, fill="orange")
myCanvas.create_line(10, 15, 50, 20, fill="black")
myCanvas.create_line(20, 5, 25, 25, fill="black")


myButton = Button(root, text="TEMPERATURE", command=tempConversionTableFC)
myButton2 = Button(root, text="QUIT", padx=23, command=closeWindow)

myCanvas.pack()

myButton.pack()

myButton2.pack()




root.mainloop()