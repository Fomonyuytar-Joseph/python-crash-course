from tkinter import *


def button_clicked():
    print("I got clicked!")
    input_text = input.get()
    my_label.config(text=input_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100 , pady=200)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50 , pady=50)

# Button
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=20)
input.insert(END, string="Placeholder Text")
input.grid(column=3, row=2)


# text = Text(height=5 , width=30)
# # text.pack()
# print(input.get())


window.mainloop()
