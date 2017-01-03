#!/usr/bin/python3
from tkinter import *
from tkinter.filedialog   import askopenfilename
fields = "Last Name", "First Name", "Distribution"

print("By using this Program, you apply to \"The Nice License\", and, that your entered details are uploaded to the internet!")
print("The details that get uploaded will appear here:")
def ChangeLog():
    win = Toplevel()
    message = """v0.1 The Kernel Update:
~-~-~-~-~-~-~-~-~-~-~-~-~
+ Added Survey 1;
+ Added Surveys Menu;
+ Added Help Menu;
+ Added Testing Menu;

v0.2 - The MOAR Update:
~-~-~-~-~-~-~-~-~-~-~-~
- Removed Testing Menu (There is testing.py);
+ Defined \"News urvey\"
+ Decided to make a changelog"""
    Label(win, text=message).pack()
    Button(win, text="Close", command=win.destroy).pack()
def messageWindow():
    win = Toplevel()
    message = "It works!"
    Label(win, text=message).pack()
    Button(win, text="OK", command=win.destroy).pack()
def Quitty():
    import time
    print("Import Quit...")
    def timer():
        time.sleep(0.5)

    t0 = time.time()
    timer()
    root.quit()
def NewFile():
    print("A new survey was created.")
    print("Review it with 'cat /dev/urandom'")
def OpenFile():
    name = askopenfilename()
    print("Your Survey gets uploaded!")
    from collections import Counter
    Counter()
    print("http://nonick.anon/download.php?id=1")
def About():
    print("About Survey")
    print("~-~-~-~-~-~-")
    print("With help of Survey you can easily make surveys.")
    print("")
    print("Guxduda: http://nonick.anon/survey.py")
def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print(("%s: '%s'" % (field, text)))

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(root, width=15, text=field, anchor="w")
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries
if __name__ == '__main__':

    root = Tk()
    root.title("Survey v0.2")
    ents = makeform(root, fields)
    root.bind("<Return>", (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text="Submit",
            command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text="Quit", command=Quitty)
    b2.pack(side=LEFT, padx=5, pady=5)
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="Surveys", menu=filemenu)
    filemenu.add_command(label="New Survey", command=messageWindow)
    filemenu.add_command(label="Open & Download", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=Quitty)
    
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Changelog", command=ChangeLog)
    helpmenu.add_command(label="About", command=About)
    
    mainloop()
