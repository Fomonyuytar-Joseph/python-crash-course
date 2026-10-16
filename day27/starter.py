from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "I change the text"
my_label.config(text="I changed it with config")


def button_clicked():
    print("I got clicked!")
    input_text = input.get()
    my_label.config(text=input_text)


# Button
button = Button(text="Click Me!", command=button_clicked)
button.pack()


# Entry
input = Entry(width=40)
input.insert(END, string="Placeholder Text")
input.pack()


text = Text(height=5 , width=30)
text.pack()
print(input.get())












window.mainloop()
