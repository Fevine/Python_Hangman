from tkinter import*

Alphabet = [
    ("e","*"),("i","**"), ("s","***"), ("h","****"),
    ("u","**-"), ("v","***-"), ("f","**-*"),
    ("a","*-"), ("r","*-*"), ("w","*--"),
    ("l","*-**"), ("p","*--*"), ("j","*---"),
    ("t","-"), ("m","--"), ("o","---"),
    ("n","-*"), ("d","-**"), ("k","-*-"),
    ("g","--*"), ("z","--**"), ("q","--*-"),
    ("b","-***"), ("x","-**-"), ("c","-*-*"), ("y","-*--")
]

root = Tk()
root.title("Morse Translator")
root.geometry("230x300")
root.resizable(True,True)
root.configure(bg='Purple')

response = StringVar()

Word = Entry(root, textvariable=response, bg='Pink')
Word.pack(expand=0)
#response.set('Enter text: ')

#label1 = Label(root,borderwidth=5, text = response.get())
#label1.pack(expand=True, anchor= NW)



def Translate(word):
    global Alphabet
    global label1
    word = word.lower()
    result = ""
    for i in range (len(word)):
        for j in range(len(Alphabet)):
            if word[i] == Alphabet [j][0]:
                result += Alphabet [j][1] + "       "
    label1 = Label(root, text=result)
    label1.pack(expand=True)

button1 = Button(root, text="Translate",bg='Grey',fg="Black",command=lambda: Translate(response.get()))
button1.pack(expand = False)

root.mainloop()