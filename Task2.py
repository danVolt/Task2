from tkinter import *
import os
import sqlite3

def loggedin():
   
    global screen2
    global name
    global branch
    global regdid
    global name_entry
    global branch_entry
    global regdid_entry

    screen2 = Toplevel(screen)
    screen2.title("Student Database")
    screen2.geometry("300x250")
    name = StringVar()
    branch = StringVar()
    regdid = StringVar()
   
   
    Label(screen2, text = "Name :").pack()
    name_entry = Entry(screen2,textvariable = name)
    name_entry.pack()
   
    Label(screen2, text = "Branch :").pack()
    branch_entry = Entry(screen2,textvariable = branch)
    branch_entry.pack()
    Label(screen2, text = "Regd Id :").pack()
    regdid_entry = Entry(screen2,textvariable = regdid)
    regdid_entry.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Submit", command = do).pack()
   


   

def open_window():
    global tip
    tip = Toplevel(screen2)
    tip.title("SUBJECTS")
    tip.geometry("300x250")
   
    Label(tip, text = "Select a subject to insert marks: ").pack()
   
    Button(tip, text = "FCT",width = 10, command = open_window_fct).pack()
   
    Button(tip, text = "IDS", width =10, command = open_window_ids).pack()

    Button(tip, text = "EMFT", width = 10, command = open_window_emft).pack()

    Label(tip, text = "").pack()

    Button(tip, text = "Submit",fg = "black",bg = "light blue",width =10, command = open_window3).pack()
   
   
def open_window_fct():
    global fct
    global fct_marks
    global fct_entry
    fct_marks = IntVar()
   
    fct = Toplevel(tip)
    fct.title("FCT")
    fct.geometry("200x100")
    Label(fct, text = "Enter the marks: ").pack()
   
    fct_entry = Entry(fct,textvariable = fct_marks)
    fct_entry.pack()
   
    Button(fct, text = "Enter", command = fct_submission).pack()
     
def fct_submission():
    Label(fct, text = "Submitted.", fg = "green").pack()
    fct1 = fct_marks.get()
    name1 = name.get()
       
    conn = sqlite3.connect("StudDB.db")
    with conn:
        cur = conn.cursor()
    cur.execute( '''UPDATE DETAILS SET FCT == "%s" WHERE Name == "%s"''' %(fct1,name1))
    conn.commit()
    cur.close()    
    conn.close()
   
   
def open_window_ids():
    global ids_marks
    global ids_entry
    global ids
    ids_marks = IntVar()
   
    ids = Toplevel(tip)
    ids.title("IDS")
    ids.geometry("200x100")
    Label(ids, text = "Enter the marks obtained :").pack()
   
    ids_entry = Entry(ids,textvariable = ids_marks)
    ids_entry.pack()
   
    Button(ids, text = "Enter", command = ids_submission).pack()
   
def ids_submission():
    Label(ids, text = "Submitted.", fg = "green").pack()        
    ids1 = ids_marks.get()
    name1 = name.get()
       
    conn = sqlite3.connect("StudDB.db")
    with conn:
        cur = conn.cursor()
    cur.execute( '''UPDATE DETAILS SET IDS == "%s" WHERE Name == "%s"''' %(ids1,name1))
    conn.commit()
    cur.close()    
    conn.close()    
 
   
def open_window_emft():
    global emft_marks
    global emft_entry
    global emft
    emft_marks = IntVar()
   
    emft = Toplevel(tip)
    emft.title("EMFT")
    emft.geometry("200x100")
    Label(emft, text = "Enter the marks obtained :").pack()
   
    emft_entry = Entry(emft,textvariable = emft_marks)
    emft_entry.pack()
    Button(emft, text = "Enter", command = emft_submission).pack()
    
def emft_submission():
    Label(emft, text = "Submitted.", fg = "green").pack()       
    emft1 = emft_marks.get()
    name1 = name.get()
   
    conn = sqlite3.connect("StudDB.db")
    with conn:
        cur = conn.cursor()
    cur.execute( '''UPDATE DETAILS SET EMFT == "%s" WHERE Name == "%s"''' %(emft1,name1))
    conn.commit()
    cur.close()    
    conn.close()   
   

 
   
def do():
    open_window()
    put()
   
def invalid():
    screen3 = Toplevel(screen)
    screen3.title("")
    screen3.geometry("150x50")
    Label(screen3, text = "Invalid UserID or Password.", fg = "red").pack()
   

def open_window3():
    global tom
    tom = Toplevel(tip)
    tom.title("GUI 3")
    tom.geometry("300x250")
   
    Label(tom, text = "").pack()
   
    Button(tom, text = "CGPA",width = 10, command = cgpa).pack()
   
    Button(tom, text = "GRADE", width =10, command = grade).pack()

    Label(tom, text = "").pack()

    Button(tom, text = "New Input", width = 10,fg = "blue", command = NewInput).pack()
   
    Button(tom, text = "Close", width = 10,fg = "red", command = close).pack()

def cgpa():
    global gpa
    scrcgpa = Toplevel(tom)
    scrcgpa.title("CGPA")
    scrcgpa.geometry("150x50")
    fctm = fct_marks.get()
    idsm = ids_marks.get()
    emftm = emft_marks.get()
    Label(scrcgpa, text = "CGPA obtained :").pack()
    gpa = (fctm + idsm + emftm)/30.0
    Label(scrcgpa,text = float(gpa)).pack()
    
    
def grade():
    scrgrade = Toplevel(tom)
    scrgrade.title("Grade")
    scrgrade.geometry("150x50")
    Label(scrgrade, text = "Grade Obtained: ").pack()
    if (gpa < 5.0):
        g = "D"
    elif(gpa < 6.0):
        g = "C"
    elif(gpa < 7.0):
        g = "B"
    elif(gpa < 8.0):
        g = "A"
    elif(gpa < 9.0):
        g = "E"
    elif(gpa < 10.1):
        g = "O"
    Label(scrgrade, text = str(g)).pack()

def NewInput():
    screen2.destroy()
    loggedin()

def close():
    screen.destroy()
 
 
conn = sqlite3.connect('StudDB.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS DETAILS(Name TEXT, Branch TEXT, RegdID INT, FCT REAL, IDS REAL, EMFT REAL)")
conn.commit()

def put():
    name1 = name.get()
    branch1 = branch.get()
    regdid1 = regdid.get()
    conn = sqlite3.connect('StudDB.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO DETAILS (Name,Branch, RegdID) VALUES (?,?,? )",(name1,branch1,regdid1))
    conn.commit()


def login_verify():
    user1 = userid.get()
    password1 = password.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
   
    list_of_files = os.listdir()
   
   
    if user1 in list_of_files:
       
        file1 = open(user1, "r")
        verify = file1.read().splitlines()
       
        if password1 in verify:
           
            loggedin()
           
        else:
            invalid()
    else:
        invalid()


def signin():
    global screen
    global userid
    global password
    global username_entry
    global password_entry
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Student Management system")  
    Label(screen, text = "Username :").pack()
    userid = StringVar()
    username_entry = Entry(textvariable = userid)
    username_entry.pack()
    Label(screen, text = "Password :").pack()
    password = StringVar()
    password_entry = Entry(textvariable = password, show = "*")
    password_entry.pack()
    Button(screen, text = "Submit", command = login_verify).pack()
    screen.mainloop()
   

signin()
cur.close()
conn.close()