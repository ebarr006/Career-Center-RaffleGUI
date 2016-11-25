# Raffle Project
# Created for UCR Career Center
# Written by Emilio Barreiro

from Tkinter import *
import tkMessageBox
from random import randint

class student:
    def __init__ (self, fullName, sid):
        self.fullName = fullName
        self.sid = sid

    def printInfo(self):
        print ("%s | %s" % (self.fullName, self.sid))

# ------------- Debugging Functions ------------- #
    def printName(self):
        print ("Name: %s" % (self.fullName))

    def printSID(self):
        print ("SID: %s" % (self.sid))
# ----------------------------------------------- #


participants = []
user = "admin"
password = "pass"

# submitEntry function for button use
def submitEntryButton():
   p1 = e1.get()
   p2 = e2.get()
   p3 = e3.get()
   name = p1 + " " + p2
   temp = student(name, p3)
   participants.append(temp)
   e1.delete(0, END)
   e2.delete(0, END)
   e3.delete(0, END)

# submitEntry function for button use
def submitEntry(self):
   p1 = e1.get()
   p2 = e2.get()
   p3 = e3.get()
   name = p1 + " " + p2
   temp = student(name, p3)
   participants.append(temp)
   e1.delete(0, END)
   e2.delete(0, END)
   e3.delete(0, END)

def authenticate():
    verify = Tk()
    h1 = 100
    w1 = 400
    screen_h1 = master.winfo_screenheight()
    screen_w1 = master.winfo_screenwidth()
    x1 = (screen_w1/2) - (w1/2)
    y1 = (screen_h1/2) - (h1/2)
    verify.geometry('%dx%d+%d+%d' % (w1, h1, x1, y1))
    verify.title("Authorize")
    Label(verify, text="Admin").grid(row=0, column=0)
    Label(verify, text="Password").grid(row=1, column=0)
    v1 = Entry(verify)
    v2 = Entry(verify, show="*")
    v1.grid(row=0, column=1)
    v2.grid(row=1, column=1)
    Button(verify, text="Submit", command=lambda: checkCred(verify, v1.get(), v2.get())).grid(row=3, column=2, sticky=W, pady=4)

def checkCred(box, one, two):
    if one == user:
        check1 = True
    else:
        check1 = False
    if two == password:
        check2 = True
    else:
        check2 = False
    if check1 == True and check2 == True:
        box.destroy()
        chooseWinner()
    else:
        box.destroy()
        tkMessageBox.showinfo( "Error", "The username or password you entered is invalid. Please try again.")

def chooseWinner():
    for student in participants:
        student.printInfo()

    select = randint(0, len(participants) - 1)
    print "WINNER -->", participants[select].printInfo()
    master.destroy()


master = Tk()
h = 170
w = 680
screen_h = master.winfo_screenheight()
screen_w = master.winfo_screenwidth()
x = (screen_w/2) - (w/2)
y = (screen_h/2) - (h/2) - 100
master.geometry('%dx%d+%d+%d' % (w, h, x, y))

photo = PhotoImage(file="emilio_logo.gif")
picture = Label(master, image=photo).grid(row=1, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, ipadx=7, padx=5, pady=5)

master.title("Career Center Raffle!")
Label(master, text="First Name").grid(row=0, column=0, padx=5, pady=5, ipady = 10, ipadx = 5)
Label(master, text="Last Name").grid(row=1, column=0, padx=5, pady=5)
Label(master, text="SID").grid(row=2, column=0, padx=5, pady=5)

Button(master, text="Done", command=authenticate, width=7).grid(row=3, column=1, sticky=W)
Button(master, text="Submit", command=submitEntryButton, width=7).grid(row=3, column=1, sticky=E)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e3.bind('<Return>', submitEntry)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)




mainloop( )
