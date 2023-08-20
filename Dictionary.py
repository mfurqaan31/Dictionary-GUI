import sys
from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
import nltk
from nltk.corpus import wordnet

root=Tk()
root.title("Dictionary")
root.resizable(False,False)
root.geometry("700x700")
root.config(bg="black")

def Find():

    text.config(state=NORMAL)
    text.delete(1.0,END)
    data=entry.get()
    if not data:
        text.insert(END,"Please enter a word")
    else:
        meaning=wordnet.synsets(data)

        if not meaning:
            text.insert(END,"The word "+data+" does not exist")    

        else:
            text.insert(END,"The meaning of "+data+" is:\n")
    
            for i in meaning:
                x=i.definition()
                text.insert( END,("->"+x+"\n") ) 
            text.insert(END,"\n")
            text.insert(END,"The synonyms of "+data+" are:\n")

            for i in meaning:
                for j in i.lemmas():
                    x=j.name()
                    text.insert(END, ( (x+"\n").replace( "_"," ") ) ) 
    
    text.config(state=DISABLED)


def Exit():
    sys.exit()


Label1=Label(root, text="Welcome to my English Dictionary",bg="black",fg="#cfff04",font=40)
Label1.pack()

Label2=Label(root, text="Enter any word to get it's meaning and synonynm",bg="black",fg="#cfff04",font=40,pady=10)
Label2.pack()

Label3=Label(root, text="Enter the word",bg="black",fg="#cfff04",font=40)
Label3.pack(pady=10)

entry=Entry(root, width=50, font=50)
entry.pack(pady=10)

button=Button(root,text="Next",bg="black",fg="#cfff04",font=40, command=Find)
button.pack()

text=scrolledtext.ScrolledText(root, height=20, width=65, wrap=WORD, state=DISABLED)
text.pack(pady=30)

exiting=Button(root, text="Quit",bg="black",fg="#cfff04",font=40, command=Exit)
exiting.pack()

root.mainloop()
