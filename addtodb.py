from tkinter import *
import sqlite3
import tkinter.messagebox

# Establish connection to the SQLite database
conn = sqlite3.connect(r'C:\Users\Ashwanth Kalyan\OneDrive\Desktop\Ashwanth\Projects\SToreManagement software\store.db')
c = conn.cursor()

# Define the Database class


class Database:
    def __init__(self, master,*args):
        self.master = master
        self.master.title("Add to the Database")
        self.master.geometry("600x400")  # Adjusted dimensions for better layout


        # Heading Label
        self.heading = Label(master, text="Add to the Database", font=("Arial", 24, "bold"), fg="blue")
        self.heading.pack(pady=20)

        self.name=Label (master,text="Name",font=("arial",24,"bold"))
        self.name.place(x=0,y=70)

        self.Count = Label(master,text="Count",font=("arial",24,"bold"))
        self.Count.place(x=0,y=120)

        self.Available = Label(master,text="Available",font=("arial",24,"bold"))
        self.Available.place(x=0,y=170)

        self.Id = Label(master,text="Id",font=("arial",24,"bold"))
        self.Id.place(x=0,y=220)

        self.Vendor = Label(master,text="Vendor",font=("arial",24,"bold"))
        self.Vendor.place(x=0,y=270)

        self.name_e=Entry(master, width=20,font=("arial",24))
        self.name_e.place(x=220,y=70)

        self.Count_e = Entry(master,width=20,font=("arial",24))
        self.Count_e.place(x=220,y=120)

        self.Available_e = Entry(master, width=20, font = ("arial",24))
        self.Available_e.place(x=220,y=170)

        self.Id_e=Entry(master,width=20,font = ("arial",24))
        self.Id_e.place(x=220,y=220)

        self.Vendor_e=Entry(master,font=("arial",24))
        self.Vendor_e.place(x=220,y=270)

        self.btn_e=Button(master,fg="Blue",text="Add to Database",width=24,bg="Pink",command=self.get_items)
        self.btn_e.place(x=320,y=320)

        self.Tbox = Text(master,width=30,height=15)
        self.Tbox.place(x=600,y=70)

    def get_items(self,*args):
        self.name=self.name_e.get()
        self.Count=self.Count_e.get()
        self.Available=self.Available_e.get()
        self.Id=self.Id_e.get()
        self.Vendor=self.Vendor_e.get()

        if self.name=="" or self.Count=="" or self.Available == "" or self.Id=="" or self.Vendor == "":
            tkinter.messagebox.showinfo("Error","Please enter all fields")
        
        else:
            sql = "INSERT into inventory (name,Count,Available,Id,Vendor) Values (?,?,?,?,?)"
            c.execute(sql,(self.name,self.Count,self.Available,self.Id,self.Vendor))
            conn.commit()

            tkinter.messagebox.showinfo("Message","Successful")

        
class Login_page:
    def __init__(self,master,*args):
        
        self.master=master
        self.master.title("login")
        
        self.heading=Label(master,text="Login Page",font=("Arial",24),fg="Steel Blue")
        self.heading.pack(pady=5)

        self.username_label=Label(master,text="Username",font=("Arial",24),fg="red")
        self.username_label.pack(pady=5)

        self.username_e=Entry(master)
        self.username_e.pack(pady=5)

        self.password_label=Label(master,text="Password",font=("Arial",24),fg="red")
        self.password_label.pack(pady=5)

        self.password_e=Entry(master)
        self.password_e.pack(pady=5)

        Login_btn=Button(master,text=("Click after here to login"),font=("arial",24),width=20,command=self.check_login,background="light pink")
        Login_btn.pack(pady=5)

        

    def start_mainapp(self):s
            Details_root=Tk()
            details_page=Database(Details_root)
            Details_root.mainloop()

    def check_login(self):
            username=self.username_e.get()
            pwd=self.password_e.get()

            if(username=="Admin" and pwd == "123"):
                print("succesful Login")

                self.master.destroy()
                self.start_mainapp()

            else:
                tkinter.messagebox.showinfo(title=("Error"),message=("Invalid Credentials"))


# Create the Tkinter root window
root = Tk()
app = Login_page(root)

# Run the application
root.mainloop()