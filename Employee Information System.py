# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:03:15 2020

@author: asus
"""


from tkinter import Label,Button,Tk,StringVar,ttk,END
import csv

filename= "Employees"
file = open(filename + ".csv","w")
cw = csv.writer(file)
fields = ["Firstname","Lastname","Age","Salary","Empid","Rank","Bldgrp","Gender"]
cw.writerow(fields)
file.close()
print("Welcome to the Employee Information System")
print()
authkey1 = input("Please create an authorization key to continue :")



def info():
    authorization = authkey.get()
    if authorization == authkey1:
        firstname1=firstname.get()
        lastname1=lastname.get()
        age1=age.get()
        salary1=salary.get()
        empid1=empid.get()
        rank1=rank.get()
        bldgrp1=bloodgrp.get()
        gender1=gender.get()
        file = open(filename + ".csv","a")
        cw = csv.writer(file)
        newrow = [firstname1,lastname1,age1,salary1,empid1,rank1,bldgrp1,gender1]
        cw.writerow(newrow)
        
    
        firstname_entry.delete(0,len(firstname1))
        lastname_entry.delete(0,len(lastname1))
        age_entry.delete(0,len(age1))
        salary_entry.delete(0,len(salary1))
        empid_entry.delete(0,len(empid1))
        rank_entry.delete(0,len(rank1))
        authkey_entry.delete(0,END)
        bloodgrp.set("Blood Group")
        gender.set("Male")
    
    else:
        print("Please enter valid Authorization Key!")
    
    

def existinguser():

    authorization = authkey.get()

    if authorization == authkey1:
        firstname_entry.delete(0,END)
        lastname_entry.delete(0,END)
        age_entry.delete(0,END)
        salary_entry.delete(0,END)
        empid_entry.delete(0,END)
        rank_entry.delete(0,END)
        authkey_entry.delete(0,END)
        bloodgrp.set("Blood Group")
        gender.set("Male")
        firstnameretrieve1=firstname_retrieve.get()
        lastnameretrieve1=lastname_retrieve.get()
        file = open("Employees" + ".csv","r")
        cw = csv.reader(file)
        next(cw)
        l = []
        for i in cw:
            l.append(i)
        
        for r in range(1,len(l),2):   
            if l[r][0] == firstnameretrieve1 and l[r][1] == lastnameretrieve1:
                    firstname_entry.insert(0,l[r][0])
                    lastname_entry.insert(0,l[r][1])
                    age_entry.insert(0,l[r][2])
                    salary_entry.insert(0,l[r][3])
                    empid_entry.insert(0,l[r][4])
                    rank_entry.insert(0,l[r][5])
                    bloodgrp.set(l[r][6])
                    gender.set(l[r][7])
        
    else:
        print("Please enter valid Authorization Key!")





def displayall():
    authorization = authkey.get()

    if authorization == authkey1:
        file = open("Employees" + ".csv","r")
        cw = csv.reader(file)
        l = []
        for i in cw:
            l.append(i)
            next(cw)

        print(l)
    else:
        print("Please enter valid Authorization Key!")
    authkey_entry.delete(0,END)




def backupfile():
    filename = backup.get()
    authorization = authkey.get()
    l = []
    if authorization == authkey1:
        file = open("Employees" + ".csv","r")
        cw = csv.reader(file)
        for i in cw:
            l.append(i)
            next(cw)
        
        with open(filename + ".csv","w") as backupfile:
            cw1 = csv.writer(backupfile)
            cw1.writerows(l)
            backupfile.close()
            print("Backup file named ",filename," is created successfully !")
    else:
        print("Please enter valid Authorization Key!")
    authkey_entry.delete(0,END)
    
def leave():
    quit()
    screen.destroy()

screen = Tk()
screen.geometry("700x700")
screen.title("Employee Information Management System")
screen.configure(bg= "RoyalBlue2")
heading = Label(screen,text = "Employee Information Management System" ,bg="gray25",fg="white",width="700",height="3")
heading.pack()
firstname_text = Label(screen,text="Firstname :" , bg="SteelBlue1")
lastname_text = Label(screen,text="Lastname :", bg="SteelBlue1")
age_text = Label(screen,text="Age :", bg="SteelBlue1")
retrieve_text = Label(screen,text = "Want to work with an exisiting employees data? Use the boxes below :", bg="seashell2")
newusr_text = Label(screen,text = "To enter data for a new employee:",bg="seashell2",width = "30")
salary_text = Label(screen,text = "Salary :", bg="SteelBlue1")
empid_text = Label(screen,text = "Employee ID :",bg="SteelBlue1")
rank_text = Label(screen,text = "Designation :",bg="SteelBlue1")
firstnameretrieve_text = Label(screen,text = "Firstname :",bg="SteelBlue1")
lastnameretrieve_text = Label(screen,text = "Lastname :",bg="SteelBlue1")
authkey_text = Label(screen,text="Authorization Key :" ,bg="SteelBlue1")
bldgrp_text = Label (screen,text = "Blood Group :" ,bg="SteelBlue1")
gender_text = Label(screen,text = "Gender :" ,bg="SteelBlue1")
line_label = Label(screen,bg = "gray25",fg="white",width="700",height="2")
backuptext1 = Label(screen,text = "The data gets deleted when you close the program\nSave this data in a backup file here :\n \n \n",bg = "SteelBlue1")
displayouterlabel = Label(screen,text = "Click here to display all the records :",bg = "seashell2")


firstname_text.place(x= 15 , y=100)
lastname_text.place(x= 15 , y=170)
age_text.place(x= 15 , y=240)
retrieve_text.place(x=15, y=480)
newusr_text.place(x=15,y=60)
salary_text.place(x=370 , y=100)
empid_text.place(x=370 ,y=170)
rank_text.place(x=370 ,y=240)
firstnameretrieve_text.place(x=15 ,y=530)
lastnameretrieve_text.place(x=15,y=570)
authkey_text.place(x=440 ,y=480)
bldgrp_text.place(x=15 ,y=310)
line_label.place(x=0,y=670)
backuptext1.place(x=420, y=525)
gender_text.place(x=370 ,y=310)
displayouterlabel.place(x = 340,y = 635)


firstname = StringVar()
firstname_retrieve = StringVar()
lastname = StringVar()
lastname_retrieve = StringVar()
age = StringVar()
salary = StringVar()
empid = StringVar()
rank=StringVar()
authkey = StringVar()
bloodgrp = StringVar()
bloodgrp.set("Blood Group")
Dateofbirth = StringVar()
gender = StringVar()
gender.set("Male")
backup = StringVar()

firstname_entry = ttk.Entry(screen,textvariable = firstname, width = "50")
lastname_entry = ttk.Entry(screen,textvariable = lastname, width = "50")
age_entry = ttk.Entry(screen,textvariable = age, width = "50")
salary_entry = ttk.Entry(screen,textvariable = salary,width = "50")
empid_entry = ttk.Entry(screen,textvariable = empid,width = "50")
rank_entry = ttk.Entry(screen,textvariable = rank,width = "50")
firstnameretrieve_entry = ttk.Entry(screen,textvariable = firstname_retrieve,width = "50")
lastnameretrieve_entry = ttk.Entry(screen,textvariable = lastname_retrieve,width="50")
authkey_entry = ttk.Entry(screen,textvariable = authkey,width = "20")
backup_entry = ttk.Entry(textvariable = backup,width = "20")



bloodgroups = ["A","B","AB","O"]
bldgrp_combo = ttk.Combobox(screen,textvariable = bloodgrp,value = bloodgroups)

genders = ["Male","Female"]
gender_combo = ttk.Combobox(screen,textvariable = gender,value = genders)

firstname_entry.place(x=15 , y=130)
lastname_entry.place(x=15 , y=200)
age_entry.place(x=15 , y=270)
salary_entry.place(x=370 , y=130)
empid_entry.place(x=370 , y=200)
rank_entry.place(x=370 , y=270)
lastnameretrieve_entry.place(x=100,y=570)
firstnameretrieve_entry.place(x=100,y=530)
authkey_entry.place(x=550,y=480)
backup_entry.place(x=440,y=570)
gender_combo.place(x=370,y=340)
bldgrp_combo.place(x=15 ,y=340)

submit = Button(screen,text = "Submit", width = "30",height = "1",command= info , bg = "DodgerBlue2")
submit.place(x=220,y=390)


retrievebutton = Button(screen,text = "Retreive Data",command = existinguser, bg = "DodgerBlue2")
retrievebutton.place(x=200 , y=615)



showallbutton = Button(text = "Display all the Records",command = displayall,bg = "DodgerBlue2")
showallbutton.place(x = 550,y = 635)


backupbutton = Button(screen,text = "Create Backup",command=backupfile ,bg="DodgerBlue2")
backupbutton.place(x=580 ,y=570)

exit_button = ttk.Button(text = "           Exit           ",command = leave)
exit_button.place(x = 300,y = 673)

screen.mainloop()