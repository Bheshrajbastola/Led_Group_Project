from tkinter import *
from tkinter import messagebox
import sqlite3 as sql


###############Database######################

con = sql.connect(database="studentdb.sqlite")
cursor = con.cursor()
try:
    '''cursor.execute("create table students"
                   "(stu_id int,"
                   "stu_name text, "
                   "stu_mob text,"
                   "stu_course text,"
                   "reg_fee int,"
                   "bal int)")

    cursor.execute("create table course(course_name text ,course_fee int)")'''
    con.commit()

except Exception as e:
    print(e)
con.close()

#########################Window##################

root = Tk()
root.state('zoomed')
root.title("Tuition Centre Management System ")
root.iconbitmap('C:/Users/Dell/Desktop/tution.ico')

root.resizable(width=False, height=False)
header_fem = Frame(root)
header_fem.configure(bg='red')
header_fem.place(x=0, y=0, relwidth=1, relheight=0.2)

title_lbl = Label(header_fem, text='Tuition Centre Management System', bg='red',
                  font=('courier', 50, 'bold', 'underline'))
title_lbl.pack()


#################Login Page########################

def main_body():
    def login():
        u = user_entry.get()
        p = pass_entry.get()
        if len(u) == 0 or len(p) == 0:
            messagebox.showwarning('login gate', "The field Can't Be Empty")
        else:
            if u == "admin" and p == "admin":
                frm.destroy()
                login_body()
            else:
                messagebox.showerror('Login gate', "Invalid UserName/Password")

    frm = Frame(root)
    frm.configure(bg='green')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    user_lbl = Label(frm, text='UserName', bg='green', font=('Arial', 20, 'bold'))
    user_lbl.place(relx=0.3, rely=0.2)

    user_entry = Entry(frm, font=('', 20, 'bold'), bd=7)
    user_entry.focus()
    user_entry.place(relx=0.45, rely=0.2)

    pass_lbl = Label(frm, text='Password', bg='green', font=('Arial', 20, 'bold'))
    pass_lbl.place(relx=0.3, rely=0.35)

    pass_entry = Entry(frm, font=('', 20, 'bold'), bd=7, show='*')
    pass_entry.place(relx=0.45, rely=0.35)

    log_btn = Button(frm, text='LogIn', font=('Arial', 20, 'bold'), bd=7, command=login)
    log_btn.place(relx=0.5, rely=0.5)


########################Button Main#########################

def login_body():
    def logout():
        frm.destroy()
        main_body()


    frm = Frame(root)
    frm.configure(bg='light green')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome To Oxford Tuition Centre", font=('Arial', 15, 'bold'), bg='light green')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Arial', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)



root.mainloop()