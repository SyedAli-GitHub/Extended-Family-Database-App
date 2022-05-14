from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import re

con = sqlite3.connect('Family.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS family (Member_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Name VARCHAR, Father_Name VARCHAR, Mother_Name VARCHAR, Phone_Number VARCHAR, Facebook VARCHAR, 
            Email VARCHAR, Current_Address VARCHAR)''')
con.commit()
con.close()

class Family:
    def __init__(self,root):
        self.root=root
        self.root.title("")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root, text="Family Database App ", bd=10, relief=GROOVE,
                      font=("times new roman", 36, "bold"), bg="skyblue", fg="navy")
        title.pack(side=TOP, fill=X)

        # ==============All Variables=======================

        self.Member_ID_var = StringVar()
        self.Name_var = StringVar()
        self.Father_Name_var = StringVar()
        self.Mother_Name_var = StringVar()
        self.Phone_Number_var = StringVar()
        self.Facebook_var = StringVar()
        self.Email_var = StringVar()
        self.Current_Address_var = StringVar()

        self.Search_By = StringVar()
        self.Search_txt = StringVar()

        # ============Manage Frame==========================
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="royalblue")
        Manage_Frame.place(x=10, y=80, width=470, height=610)

        m_title = Label(Manage_Frame, text="Insert Member Information", bg="royalblue", fg="white",
                        font=("times new roman", 28, "bold"))
        m_title.grid(row=0, columnspan=2, pady=16)

        # lbl_Member_ID = Label(Manage_Frame, text="Member_ID", bg="royalblue", fg="white",font=("times new roman", 20, "bold"))
        # lbl_Member_ID.grid(row=1, column=0, pady=8, padx=5, sticky="w")

        # txt_Member_ID = Entry(Manage_Frame, textvariable=self.Member_ID_var, font=("times new roman", 15, "bold",),bd=5, relief=GROOVE)
        # txt_Member_ID.grid(row=1, column=1, pady=8, padx=5, sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name", bg="royalblue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=5, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold",), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=5, sticky="w")

        lbl_Father_Name = Label(Manage_Frame, text="Father_Name", bg="royalblue", fg="white",
                               font=("times new roman", 20, "bold"))
        lbl_Father_Name.grid(row=3, column=0, pady=10, padx=5, sticky="w")

        txt_Father_Name = Entry(Manage_Frame, textvariable=self.Father_Name_var, font=("times new roman", 15, "bold",),
                               bd=5, relief=GROOVE)
        txt_Father_Name.grid(row=3, column=1, pady=10, padx=5, sticky="w")

        lbl_Mother_Name = Label(Manage_Frame, text="Mother_Name", bg="royalblue", fg="white",
                                   font=("times new roman", 20, "bold"))
        lbl_Mother_Name.grid(row=4, column=0, pady=10, padx=5, sticky="w")

        txt_Mother_Name = Entry(Manage_Frame, textvariable=self.Mother_Name_var,
                                   font=("times new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_Mother_Name.grid(row=4, column=1, pady=10, padx=5, sticky="w")

        lbl_Phone_Number = Label(Manage_Frame, text="Phone_Number", bg="royalblue", fg="white",
                                    font=("times new roman", 20, "bold"))
        lbl_Phone_Number.grid(row=5, column=0, pady=10, padx=5, sticky="w")

        txt_Phone_Number = Entry(Manage_Frame, textvariable=self.Phone_Number_var,
                                    font=("times new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_Phone_Number.grid(row=5, column=1, pady=10, padx=5, sticky="w")

        lbl_Facebook = Label(Manage_Frame, text="Facebook", bg="royalblue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Facebook.grid(row=6, column=0, pady=10, padx=5, sticky="w")

        txt_Facebook = Entry(Manage_Frame, textvariable=self.Facebook_var, font=("times new roman", 15, "bold",), bd=5,
                          relief=GROOVE)
        txt_Facebook.grid(row=6, column=1, pady=10, padx=5, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="royalblue", fg="white",
                                 font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=7, column=0, pady=10, padx=5, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var,
                                 font=("times new roman", 15, "bold",), bd=5, relief=GROOVE)
        txt_Email.grid(row=7, column=1, pady=10, padx=5, sticky="w")

        lbl_Current_Address = Label(Manage_Frame, text="Current_Address", bg="royalblue", fg="white",
                                    font=("times new roman", 20, "bold"))
        lbl_Current_Address.grid(row=8, column=0, pady=10, padx=5, sticky="w")

        self.txt_Current_Address = Text(Manage_Frame, width=30, height=3, font=("", 10))
        self.txt_Current_Address.grid(row=8, column=1, pady=10, padx=5, sticky="w")

        # ==============Button Frame========================

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="navy")
        btn_Frame.place(x=5, y=520, width=454)

        addbtn = Button(btn_Frame, text="Add", font="bold", width=10, command=self.add_member).grid(row=0, column=0, padx=4, pady=10)
        updatebtn = Button(btn_Frame, text="Update", font="bold", width=10, command=self.update_data).grid(row=0, column=1, padx=7,pady=10)
        deletebtn = Button(btn_Frame, text="Delete", font="bold", width=10, command=self.delete_data, state=DISABLED).grid(row=0, column=2, padx=7,pady=10)
        clearbtn = Button(btn_Frame, text="Clear", font="bold", width=10, command=self.clear).grid(row=0, column=3, padx=5, pady=10)

        # ============Detail Frame==========================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="navy")
        Detail_Frame.place(x=490, y=80, width=900, height=610)

        lbl_search = Label(Detail_Frame, text="Search By", bg="navy", fg="white",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.Search_By, width=15,font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Member_ID", "Name", "Father_Name", "Mother_Name", "Phone_Number", "Facebook", "Email","Current_Address")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, textvariable=self.Search_txt, width=20, font=("times new roman", 10, "bold",),bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", font="bold", width=14, pady=5, command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", font="bold", width=14, pady=5, command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        # =========Table Frame======================

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="navy")
        Table_Frame.place(x=5, y=70, width=860, height=520)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.member_table = ttk.Treeview(Table_Frame, columns=("Member_ID", "Name", "Father_Name", "Mother_Name", "Phone_Number", "Facebook", "Email","Current_Address"), xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.member_table.xview)
        scroll_y.config(command=self.member_table.yview)
        self.member_table.heading("Member_ID", text="Member_ID")
        self.member_table.heading("Name", text="Name")
        self.member_table.heading("Father_Name", text="Father_Name")
        self.member_table.heading("Mother_Name", text="Mother_Name")
        self.member_table.heading("Phone_Number", text="Phone_Number")
        self.member_table.heading("Facebook", text="Facebook")
        self.member_table.heading("Email", text="Email")
        self.member_table.heading("Current_Address", text="Current_Address")
        self.member_table["show"] = 'headings'
        self.member_table.column("Member_ID", width=65)
        self.member_table.column("Name", width=110)
        self.member_table.column("Father_Name", width=85)
        self.member_table.column("Mother_Name", width=90)
        self.member_table.column("Phone_Number", width=95)
        self.member_table.column("Facebook", width=110)
        self.member_table.column("Email", width=90)
        self.member_table.column("Current_Address", width=150)
        self.member_table.pack(fill=BOTH, expand=1)
        self.member_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    def add_member(self):
        if self.Name_var.get() == "" or self.Father_Name_var.get() == "":
            messagebox.showerror("Error", "Name and Father's Name Fields Are Required!!")
        else:
            con = sqlite3.connect('Family.db')
            c = con.cursor()
            c.execute("INSERT INTO family VALUES (NULL,?,?,?,?,?,?,?)", (
                                                                                    self.Name_var.get(),
                                                                                    self.Father_Name_var.get(),
                                                                                    self.Mother_Name_var.get(),
                                                                                    self.Phone_Number_var.get(),
                                                                                    self.Facebook_var.get(),
                                                                                    self.Email_var.get(),
                                                                                    self.txt_Current_Address.get('1.0',
                                                                                                                 END)
                                                                                    ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Required Records Have Been Inserted Successfully!!")

    def fetch_data(self):
        con = sqlite3.connect('Family.db')
        c = con.cursor()
        c.execute("select * from family")
        rows=c.fetchall()
        if len(rows)!=0:
            self.member_table.delete(*self.member_table.get_children())
            for row in rows:
                self.member_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear(self):
        self.Member_ID_var.set("")
        self.Name_var.set("")
        self.Father_Name_var.set("")
        self.Mother_Name_var.set("")
        self.Phone_Number_var.set("")
        self.Facebook_var.set("")
        self.Email_var.set("")
        self.txt_Current_Address.delete('1.0', END)

    def get_cursor(self, ev):
        cursor_row = self.member_table.focus()
        contents = self.member_table.item(cursor_row)
        row = contents['values']
        self.Member_ID_var.set(row[0])
        self.Name_var.set(row[1])
        self.Father_Name_var.set(row[2])
        self.Mother_Name_var.set(row[3])
        self.Phone_Number_var.set(row[4])
        self.Facebook_var.set(row[5])
        self.Email_var.set(row[6])
        self.txt_Current_Address.delete("1.0", END)
        self.txt_Current_Address.insert(END, row[7])

    def update_data(self):
        con = sqlite3.connect('Family.db')
        c = con.cursor()
        c.execute("UPDATE family SET Name=?,Father_Name=?,Mother_Name=?,Phone_Number=?,Facebook=?,Email=?,Current_Address=? where Member_ID=?",(
                                                                                                                                        self.Name_var.get(),
                                                                                                                                        self.Father_Name_var.get(),
                                                                                                                                        self.Mother_Name_var.get(),
                                                                                                                                        self.Phone_Number_var.get(),
                                                                                                                                        self.Facebook_var.get(),
                                                                                                                                        self.Email_var.get(),
                                                                                                                                        self.txt_Current_Address.get('1.0',END),
                                                                                                                                        self.Member_ID_var.get()
                                                                                                                                        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = sqlite3.connect('Family.db')
        c = con.cursor()
        c.execute("delete from family where Member_ID=?",(self.Member_ID_var.get(),))
        c.execute("UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'family'")
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = sqlite3.connect('Family.db')
        c = con.cursor()

        c.execute("SELECT * from family where "+str(self.Search_By.get())+" LIKE '%"+str(self.Search_txt.get())+"%'")
        rows=c.fetchall()
        if len(rows)!=0:
            self.member_table.delete(*self.member_table.get_children())
            for row in rows:
                self.member_table.insert('', END, values=row)
                con.commit()
        con.close()



root = Tk()
ob=Family(root)
root.iconbitmap("Family.ico")
root.mainloop()
