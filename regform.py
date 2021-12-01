from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

#------labels------
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="FullName:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

label_2 = Label(root, text="Email:",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

label_3 = Label(root, text="Gender:",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

label_4 = Label(root, text="Country:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

label_5 = Label(root, text="Language:",width=20,font=("bold", 10))
label_5.place(x=70,y=330)


#-------entries---------
entry_1 = Entry(root)
entry_1.place(x=240,y=130)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

#------Radio Button--------
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

#------droplet-----------
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

#-----Checkbox----------
var1 = IntVar()
Checkbutton(root, text="Telugu", variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(root, text="English", variable=var2).place(x=300,y=330)

#------Button---------
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
