import os.path
import smtplib
import time
import tkinter.messagebox
import inventory_Back
from tkinter import *
 
def stmain_screen():    #student teacher screen
  global stscreen
  stscreen = Tk()
  
  stscreen.geometry("300x250")
  stscreen.title("CALIBRE PORTAL")

  Label(text = "CALIBRE PORTAL 1.0", bg = "#BF3EFF", width = "300", height = "2", font = ("Segoe Script", 13)).pack()
  Label(text = "").pack()
  Button(text = "Student", height = "2", width = "30", command = student).pack()
  Label(text = "").pack()
  Button(text = "Teacher",height = "2", width = "30", command = teacher).pack()
 
  stscreen.mainloop()

def student():     #STUDENT BUTTON
    global choice
    choice="Student"
    main_screen()
def teacher():  #TEACHER BUTTON
    
    global choice
    choice="Teacher"
    main_screen()
    
def main_screen():  #login register screen
  global screen
  screen = Toplevel(stscreen) 
  screen.geometry("300x250")
  screen.title("CALIBRE PORTAL")
  Label(screen, text = "CALIBRE PORTAL 1.0", bg = "#33C1FF", width = "300", height = "2", font = ("Segoe Script", 13)).pack()
  Label(screen,text = "").pack()
  Button(screen, text = "Login", height = "2", width = "30", command = login).pack()
  Label(screen,text = "").pack()
  Button(screen,text = "Register",height = "2", width = "30", command = register).pack()
  #screen.mainloop()
  #stscreen.destroy()    #destroying student teacher screen
  
def register():     #REGISTER BUTTON
  global flag1
  flag1=False
  global screen0
  screen0 = Toplevel(screen)
  screen0.title("Register")
  screen0.geometry("300x250")
   
  global username
  global password
  global mailid
  global mail
  global username_entry
  global password_entry
  global mailid_entry
  username = StringVar()
  password = StringVar()
  mailid = StringVar()
 
  Label(screen0, text = "Please enter details below").pack()
  Label(screen0, text = "").pack()
  Label(screen0, text = "Username * ", fg='red').pack()
  username_entry = Entry(screen0, textvariable = username)
  username_entry.pack()
  Label(screen0, text = "Password * ", fg='red').pack()
  password_entry =  Entry(screen0, textvariable = password,show='*')
  password_entry.pack()
  Label(screen0, text = "Mail ID * ", fg='red').pack()
  mailid_entry = Entry(screen0, textvariable = mailid)
  mailid_entry.pack()
  Label(screen0, text = "").pack()
  Button(screen0, text = "Register", width = 10, height = 1, command = register_user).pack()
  
def register_user():     #REGISTER FUNCTION
  global flag1

  username_info = username.get()
  password_info = password.get()
  mail=mailid.get()
  print(mail)
  if(username_info == "" or password_info==""):
      return
 
  file=open(choice+username_info+".txt", "w")
  file.write(username_info+"\n")
  file.write(password_info+"\n")
  file.write(mail)
  file.close()
 
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  
  mailid_entry.delete(0, END)
  if flag1==False:
    Label(screen0, text = "Registration Success", fg = "green" ,font = ("calibri", 11)).pack()
    flag1=True
   
def login():         #LOGIN BUTTON
  global screen2
  global flag
  flag=False
  print("Login session started")
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
   
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(screen2, text = "Please enter details below").pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Username * ", fg='red').pack()
  username_entry = Entry(screen2, textvariable = username)
  username_entry.pack()
  Label(screen2, text = "Password * ", fg='red').pack()
  password_entry =  Entry(screen2, textvariable = password,show='*')
  password_entry.pack()
  
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = check_login).pack()
 
def check_login():     #LOGIN CROSS CHECK
    global flag
    global mail
    if not os.path.isfile(choice+username.get() +".txt"):
       if not flag:
         Label1=Label(screen2, text = "Invalid Username or Password", fg = "red" ,font = ("Calibri", 11)).pack()
         flag=True
       username_entry.delete(0, END)
       password_entry.delete(0, END)
           
    else:
        with open(choice+username.get() +".txt") as f:
            data = f.readlines() 
            uname = data[0].rstrip() 
            pword = data[1].rstrip()
            mail = data[2].rstrip()
        if choice=="Student":          #STUDENT OPTION
          
            if username.get() == uname and password.get() == pword: 
                #r = Tk()
                global s
                s=Toplevel(screen)
                s.geometry("300x250")
                s.title("Calibre PORTAL")
                Label(s,text = "CALIBRE PORTAL 1.0", bg = "#33C1FF", width = "300", height = "2", font = ("Segoe Script", 13)).pack()
                Label(s,text = "").pack()
                Button(s,text = "Student Discussion", height = "2", width = "30",command=sdiscussion).pack() #
                Label(s,text = "").pack()
                Button(s,text = "Teacher Discussion", height = "2", width = "30", command=tdiscussion).pack() #
                Label(s,text = "").pack()
                s.mainloop()
                screen.destroy()
                #screen2.destroy()
            
                '''
                r.title('Success')
                r.geometry('100x100') 
                rlbl = Label(r, text='\n[+] Logged In')
                rlbl.pack()
                '''
            else:
               if not flag:
                 Label1=Label(screen2, text = "Invalid Username or Password", fg = "red" ,font = ("calibri", 11)).pack()
                 flag=True
               username_entry.delete(0, END)
               password_entry.delete(0, END)
        else:                              #TEACHER OPTION
            if username.get() == uname and password.get() == pword: 
                s=Toplevel(screen)
                s.geometry("300x250")
                s.title("CALIBRE PORTAL")
                Label(s,text = "CALIBRE PORTAL 1.0", bg = "#33C1FF", width = "300", height = "2", font = ("Segoe Script", 13)).pack()
                Label(s,text = "").pack()
                Button(s,text = "Inventory", height = "2", width = "30", command=Inventory).pack() #
                Label(s,text = "").pack()
                Button(s,text = "Student Medical Registration Form", height = "2", width = "30", command=MRF).pack() #
                Label(s,text = "").pack()
                s.mainloop()
                screen.destroy()
                #screen2.destroy()
            
                '''
                r.title('Success')
                r.geometry('100x100') 
                rlbl = Label(r, text='\n[+] Logged In')
                rlbl.pack()
                '''
            else:
               if not flag:
                 Label1=Label(screen2, text = "Invalid Username or Password", fg = "red" ,font = ("calibri", 11)).pack()
                 flag=True
               username_entry.delete(0, END)
               password_entry.delete(0, END)
def Inventory():
  import tkinter.messagebox
  import inventory_Back1
  import inventory_Back2
  def PE():
          PEroot=Tk()
          
          PEroot.geometry("1350x750+0+0")
          PEroot.config(bg="cadet blue")

          SportID=StringVar(PEroot)
          SportEquip=StringVar(PEroot)
          MusicEquip=StringVar()
          SportNum=StringVar(PEroot)
          MusicNum=StringVar()
          CompanySpo=StringVar(PEroot)
          CompanyMus=StringVar()
          #====================Main Functions==================#


          
          def iExit():
              iExit=tkinter.messagebox.askyesno("Inventory","Confirm if you want to exit")
              if iExit>0:
                      PEroot.destroy()
                      return
          def clearData():
                  txtSportID.delete(0,END)
                  txtSportequip.delete(0,END)
                  txtSportCom.delete(0,END)
                  txtSportNo.delete(0,END)

          def addData():
                  if len(SportID.get())!=0:
                          inventory_Back1.addPEInfo(SportID.get(),SportEquip.get(),CompanySpo.get(),SportNum.get())
                          
                          PElist.delete(0,END)

                          PElist.insert(END,(SportID.get(),SportEquip.get(), CompanySpo.get(),SportNum.get()))

          def displayData():
                  PElist.delete(0,END)
                  for row in inventory_Back1.viewData():
                          PElist.insert(END,row,str(""))
          def PErec(event):
                 global sd
                 searchPE= PElist.curselection()[0]
                 sd=PElist.get(searchPE)

                 txtSportID.delete(0,END)
                 txtSportID.insert(END,sd[1])
                 txtSportequip.delete(0,END)
                 txtSportequip.insert(END,sd[2])
                 txtSportCom.delete(0,END)
                 txtSportCom.insert(END,sd[3])
                 txtSportNo.delete(0,END)
                 txtSportNo.insert(END,sd[4])
          def DeleteData():
                   if len(SportID.get())!=0:
                           inventory_Back1.deleteRec(sd[0])
                           clearData()
                           displayData()
          def searchDatabase():
                PElist.delete(0,END)
                for row in inventory_Back1.searchdata(SportID.get(),SportEquip.get(),CompanySpo.get(),SportNum.get()):
                        PElist.insert(END,row,str(""))
                        
                

          def updateData():
                 if len(SportID.get())!=0:
                    inventory_Back1.deleteRec(sd[0])
                 if len(SportID.get())!=0:
                          inventory_Back1.addPEInfo(SportID.get(),SportEquip.get(),CompanySpo.get(),SportNum.get())
                          PElist.delete(0,END)
                          PElist.insert(END,(SportID.get(),SportEquip.get(),CompanySpo.get(),SportNum.get()))
                 
                    
                 
                                  
                                  
                  
                  
                  
                  
          
      

          
      #=======================Frames==============#
          MainFrame= Frame(PEroot,bg="cadet blue")
          MainFrame.grid()

          TitFrame= Frame(MainFrame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
          TitFrame.pack(side=TOP)

          selflbTit= Label(TitFrame,font=('arial',87,'bold'),text="Physical Education",bg="Ghost White")
          selflbTit.grid()

          ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
          ButtonFrame.pack(side=BOTTOM)

          DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,bg="Cadet Blue",relief=RIDGE)
          DataFrame.pack(side=BOTTOM)

          DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,pady=10,bg="Ghost White",relief=RIDGE,font=('arial',20,'bold'),text="Equipment Info\n")
          DataFrameLEFT.pack(side=LEFT)

          DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,bg="Ghost White",relief=RIDGE,font=('arial',20,'bold'),text="Equipment Details\n")
          DataFrameRIGHT.pack(side=RIGHT)
      #=======================Label and Entry Widgets==============#
          lbSportID=Label(DataFrameLEFT,font=('arial',15,'bold'),text="Equipment ID:",padx=2,pady=2,bg="Ghost White")
          lbSportID.grid(row=0,column=0,sticky=W)
          txtSportID=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvar=SportID,width=39)
          txtSportID.grid(row=0,column=1)

          lbSportequip=Label(DataFrameLEFT,font=('arial',15,'bold'),text="Sport Equipment:",padx=2,pady=2,bg="Ghost White")
          lbSportequip.grid(row=1,column=0,sticky=W)
          txtSportequip=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvar=SportEquip,width=39)
          txtSportequip.grid(row=1,column=1)

          lbSportCom=Label(DataFrameLEFT,font=('arial',15,'bold'),text="Sport Company:",padx=2,pady=2,bg="Ghost White")
          lbSportCom.grid(row=2,column=0,sticky=W)
          txtSportCom=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvar=CompanySpo,width=39)
          txtSportCom.grid(row=2,column=1)
          
          lbSportNo=Label(DataFrameLEFT,font=('arial',15,'bold'),text="Amount of Equipment:",padx=2,pady=2,bg="Ghost White")
          lbSportNo.grid(row=3,column=0,sticky=W)
          txtSportNo=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvar=SportNum,width=39)
          txtSportNo.grid(row=3,column=1)
    #=======================ListBox & ScrollBar Widget==============#
          scrollbar=Scrollbar(DataFrameRIGHT)
          scrollbar.grid(row=0,column=1,sticky='ns')
          PElist= Listbox(DataFrameRIGHT, width=41, height=16, font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
          PElist.bind('<<ListboxSelect>>',PErec)          
          PElist.grid(row=0,column=0,padx=8)
          scrollbar.config(command=PElist.yview)
  #=======================Button Widget==============#
          PEroot.BtnAddData=Button(ButtonFrame, text="Add New",font=('arial',20,'bold'),width=10, height=1,bd=4,command=addData)
          PEroot.BtnAddData.grid(row=0,column=0)

          PEroot.BtnDisplayData=Button(ButtonFrame, text="Display",font=('arial',20,'bold'),width=10, height=1,bd=4,command=displayData)
          PEroot.BtnDisplayData.grid(row=0,column=1)

          PEroot.BtnClearData=Button(ButtonFrame, text="Clear",font=('arial',20,'bold'),width=10, height=1,bd=4,command=clearData)
          PEroot.BtnClearData.grid(row=0,column=2)

          PEroot.BtnDeleteData=Button(ButtonFrame, text="Delete",font=('arial',20,'bold'),width=10, height=1,bd=4,command=DeleteData)
          PEroot.BtnDeleteData.grid(row=0,column=3)

          PEroot.BtnSearchData=Button(ButtonFrame, text="Search",font=('arial',20,'bold'),width=10, height=1,bd=4,command=searchDatabase)
          PEroot.BtnSearchData.grid(row=0,column=4)

          PEroot.BtnUpdateData=Button(ButtonFrame, text="Update",font=('arial',20,'bold'),width=10, height=1,bd=4,command=updateData)
          PEroot.BtnUpdateData.grid(row=0,column=5)
          
          PEroot.BtnExitData=Button(ButtonFrame, text="Exit",font=('arial',20,'bold'),width=10, height=1,bd=4,command=iExit)
          PEroot.BtnExitData.grid(row=0,column=6)

          
  def Music():
          Muroot=Tk()
          
          Muroot.geometry("1350x750+0+0")
          Muroot.config(bg="cadet blue")

          MusicID=StringVar(Muroot)
          MusicEquip=StringVar(Muroot)
          MusicNum=StringVar(Muroot)
          CompanyMus=StringVar(Muroot)
          #====================Main Functions==================#


          
          def mExit():
              mExit=tkinter.messagebox.askyesno("Inventory","Confirm if you want to exit")
              if mExit>0:
                      Muroot.destroy()
                      return
          def MclearData():
                  txtMusicID.delete(0,END)
                  txtMusicequip.delete(0,END)
                  txtMusicCom.delete(0,END)
                  txtMusicNo.delete(0,END)

          def MaddData():
                  if len(MusicID.get())!=0:
                          inventory_Back2.addMusicInfo(MusicID.get(),MusicEquip.get(),CompanyMus.get(),MusicNum.get())
                          
                          Mulist.delete(0,END)

                          Mulist.insert(END,(MusicID.get(),MusicEquip.get(),CompanyMus.get(),MusicNum.get()))

          def MdisplayData():
                  Mulist.delete(0,END)
                  for row in inventory_Back2.viewData():
                          Mulist.insert(END,row,str(""))
          def Murec(event):
                 global sd
                 searchMu= Mulist.curselection()[0]
                 sd=Mulist.get(searchMu)

                 txtMusicID.delete(0,END)
                 txtMusicID.insert(END,sd[1])
                 txtMusicequip.delete(0,END)
                 txtMusicequip.insert(END,sd[2])
                 txtMusicCom.delete(0,END)
                 txtMusicCom.insert(END,sd[3])
                 txtMusicNo.delete(0,END)
                 txtMusicNo.insert(END,sd[4])
          def MDeleteData():
                   if len(MusicID.get())!=0:
                           inventory_Back2.deleteRec(sd[0])
                           clearData()
                           displayData()
          def MsearchDatabase():
                Mulist.delete(0,END)
                for row in inventory_Back2.searchdata(MusicID.get(),MusicEquip.get(),CompanyMus.get(),MusicNum.get()):
                        Mulist.insert(END,row,str(""))
                        
                

          def MupdateData():
                 if len(MusicID.get())!=0:
                    inventory_Back2.deleteRec(sd[0])
                 if len(MusicID.get())!=0:
                          inventory_Back2.addMusicInfo(MusicID.get(),MusicEquip.get(),CompanyMus.get(),MusicNum.get())
                          Mulist.delete(0,END)
                          Mulist.insert(END,(MusicID.get(),MusicEquip.get(),CompanyMus.get(),MusicNum.get()))
                 
                    
                 
                                  
                                  
                  
                  
                  
                  
          
      

          
      #=======================Frames==============#
          MainFrame= Frame(Muroot,bg="cadet blue")
          MainFrame.grid()

          TitFrame= Frame(MainFrame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
          TitFrame.pack(side=TOP)

          selflbTit= Label(TitFrame,font=('arial',87,'bold'),text="Music",bg="Ghost White")
          selflbTit.grid()

          ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
          ButtonFrame.pack(side=BOTTOM)

          DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,bg="Cadet Blue",relief=RIDGE)
          DataFrame.pack(side=BOTTOM)

          DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,pady=10,bg="Ghost White",relief=RIDGE,font=('arial',20,'bold'),text="Equipment Info\n")
          DataFrameLEFT.pack(side=LEFT)

          DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,bg="Ghost White",relief=RIDGE,font=('arial',20,'bold'),text="Equipment Details\n")
          DataFrameRIGHT.pack(side=RIGHT)
          
      #=======================Label and Entry Widgets==============#
          lbMusicID=Label(DataFrameLEFT,font=('arial',15,'bold'),text="Music Equipment ID:",padx=2,pady=2,bg="Ghost White")
          lbMusicID.grid(row=0,column=0,sticky=W)
          txtMusicID=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvar=MusicID,width=39)
          txtMusicID.grid(row=0,column=1)

          lbMusicequip=Label(DataFrameLEFT,font=('arial',15,'bold'),text="Music Equipment:",padx=2,pady=2,bg="Ghost White")
          lbMusicequip.grid(row=1,column=0,sticky=W)
          txtMusicequip=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvar=MusicEquip,width=39)
          txtMusicequip.grid(row=1,column=1)

          lbMusicCom=Label(DataFrameLEFT,font=('arial',15,'bold'),text="Music Company:",padx=2,pady=2,bg="Ghost White")
          lbMusicCom.grid(row=2,column=0,sticky=W)
          txtMusicCom=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvar=CompanyMus,width=39)
          txtMusicCom.grid(row=2,column=1)
          
          lbMusicNo=Label(DataFrameLEFT,font=('arial',15,'bold'),text="Amount of Equipment:",padx=2,pady=2,bg="Ghost White")
          lbMusicNo.grid(row=3,column=0,sticky=W)
          txtMusicNo=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvar=MusicNum,width=39)
          txtMusicNo.grid(row=3,column=1)
    #=======================ListBox & ScrollBar Widget==============#
          scrollbar=Scrollbar(DataFrameRIGHT)
          scrollbar.grid(row=0,column=1,sticky='ns')
          Mulist= Listbox(DataFrameRIGHT, width=41, height=16, font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
          Mulist.bind('<<ListboxSelect>>',Murec)          
          Mulist.grid(row=0,column=0,padx=8)
          scrollbar.config(command=Mulist.yview)
  #=======================Button Widget==============#
          Muroot.BtnAddData=Button(ButtonFrame, text="Add New",font=('arial',20,'bold'),width=10, height=1,bd=4,command=MaddData)
          Muroot.BtnAddData.grid(row=0,column=0)

          Muroot.BtnDisplayData=Button(ButtonFrame, text="Display",font=('arial',20,'bold'),width=10, height=1,bd=4,command=MdisplayData)
          Muroot.BtnDisplayData.grid(row=0,column=1)

          Muroot.BtnClearData=Button(ButtonFrame, text="Clear",font=('arial',20,'bold'),width=10, height=1,bd=4,command=MclearData)
          Muroot.BtnClearData.grid(row=0,column=2)

          Muroot.BtnDeleteData=Button(ButtonFrame, text="Delete",font=('arial',20,'bold'),width=10, height=1,bd=4,command=MDeleteData)
          Muroot.BtnDeleteData.grid(row=0,column=3)

          Muroot.BtnSearchData=Button(ButtonFrame, text="Search",font=('arial',20,'bold'),width=10, height=1,bd=4,command=MsearchDatabase)
          Muroot.BtnSearchData.grid(row=0,column=4)

          Muroot.BtnUpdateData=Button(ButtonFrame, text="Update",font=('arial',20,'bold'),width=10, height=1,bd=4,command=MupdateData)
          Muroot.BtnUpdateData.grid(row=0,column=5)
          
          Muroot.BtnExitData=Button(ButtonFrame, text="Exit",font=('arial',20,'bold'),width=10, height=1,bd=4,command=mExit)
          Muroot.BtnExitData.grid(row=0,column=6)
          
  class INVENTORY:
      
      def __init__(self,root):
          self.root =root
          self.root.title("Inventory")
          self.root.geometry("1350x750+0+0")
          self.root.config(bg="cadet blue")
          
         
      

          
      #=======================Frames==============#
          MainFrame= Frame(self.root,bg="cadet blue")
          MainFrame.grid()

          TitFrame= Frame(MainFrame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
          TitFrame.pack(side=TOP)

          selflbTit= Label(TitFrame,font=('arial',87,'bold'),text="Inventory for Teachers",bg="Ghost White")
          selflbTit.grid()

         

    
      #=======================Buttons==============#


       #=======================Buttons==============#
          


          but1=Button(root, text='Physical Education',font=('arial',30,'bold'),bg='yellow',command=PE)
          but1.grid()       

          but2=Button(root, text='Music',font=('arial',30,'bold'), bg='yellow',command=Music)
          but2.grid()



  if __name__=='__main__':
      root=Tk()
      application=INVENTORY(root)
      root.mainloop()
  
 

def MRF():

  global fullname
  global Email
  global Allergies
  global Description



  root1 = Tk()
  root1.geometry('500x500')
  root1.title("Medical Registration Form")

  fullname = StringVar(root1)
  Email = StringVar(root1)
  Allergies = StringVar(root1)

  Description = StringVar(root1)


  label_0 = Label(root1, text="Medical Registration form",width=20,font=("bold", 20))
  label_0.place(x=90,y=53)


  label_1 = Label(root1, text="Full Name :",width=20,font=("bold", 10))
  label_1.place(x=80,y=130)

  entry_1 = Entry(root1, textvariable=fullname)
  entry_1.place(x=240,y=130)

  label_2 = Label(root1, text="Email :",width=20,font=("bold", 10))
  label_2.place(x=68,y=180)

  entry_2 = Entry(root1, textvariable=Email)
  entry_2.place(x=240,y=180)

  label_3 = Label(root1, text="Gender :",width=20,font=("bold", 10))
  label_3.place(x=70,y=230)
  var = IntVar()
  Radiobutton(root1, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
  Radiobutton(root1, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
  if var==1:
      x="Female"
  else:
      x="Male"
  label_4 = Label(root1, text="Grade :",width=20,font=("bold", 10))
  label_4.place(x=70,y=280)

  list1 = ['1','2','3','4','5','6','7','8','9','10','11','12',]
  global c
  c=StringVar()
  droplist=OptionMenu(root1,c, *list1)
  droplist.config(width=15)
  c.set('select grade') 
  droplist.place(x=240,y=280)

  label_4 = Label(root1, text="Type of injury/sickness :",width=20,font=("bold", 10))
  label_4.place(x=100, y=325)
  var1 = IntVar()
  Checkbutton(root1, text="Minor", variable=var1).place(x=260,y=325)
  var2 = IntVar()
  Checkbutton(root1, text="Major", variable=var2).place(x=330,y=325)
  if str(var1.get)==0 and str(var2.get)==1:
    y="Minor"
  else:
    y="Major"
  label_5 = Label(root1, text="Allergies (if any) :",width=20,font=("bold", 10))
  label_5.place(x=100,y=360)
  entry_3 = Entry(root1, textvariable=Allergies)
  entry_3.place(x=250,y=364)

  label_6 = Label(root1, text="Describe illness briefly:",width=20,font=("bold", 10))
  label_6.place(x=100,y=400)
  entry_4 = Entry(root1, textvariable=Description)
  entry_4.place(x=270,y=402)

  def file():
      a1=fullname.get()
      b=Email.get()
      b2=c.get()
      f=Allergies.get()
      g=Description.get()
      file=open("MRF"+a1+".txt", "w")     #
      file.write(a1+"\n")
      file.write(b+"\n")
      file.write(x+"\n")
      file.write(b2+"\n")
      file.write(y+"\n")
      file.write(f+"\n")
      file.write(g)
      file.close()
  Button(root1, text='Submit',width=20,bg='brown',fg='white', command=file).place(x=180,y=450)



  root1.mainloop()



def sdiscussion():     #Student Discussion text
  global d
  d=Toplevel(s)
  global sDiscussion
  global sDisc_entry
  d.geometry("300x250")
  Label(d, text = "Type here", bg = "#33C1FF", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(d,text = "").pack()
  sDiscussion=StringVar()
  sDisc_entry = Entry(d, textvariable = sDiscussion)
  sDisc_entry.pack()
  Button(d,text = "Submit",height = "2", width = "30", command = email).pack()
  
def tdiscussion():      #Subject Selection Page
  global d
  d= Toplevel(s)
  d.geometry("300x300")
  Label(d, text = "Choose subject:", bg = "#33C1FF", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(d,text = "").pack()
  Button(d,text = "Physics", height = "2", width = "30",command=physics).pack()                      #
  Button(d,text = "Chemistry", height = "2", width = "30",command=chemistry).pack()                    #
  Button(d,text = "Math", height = "2", width = "30",command=math).pack()                         #
  Button(d,text = "Computer Science", height = "2", width = "30",command=cs).pack()             #
  Button(d,text = "English", height = "2", width = "30",command=english).pack()                      # 
  
def email():       #Student Discussion Mail, Python to mail function
  server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
  server.login("calibreportal", "calibreportal@2832")
  server.sendmail(
    "calibreportal@gmail.com", 
    ["nev.kd2832@gmail.com","evantferns@gmail.com"],
    sDiscussion.get()+"\n\nsent by\n"+ mail)
  server.quit()
  sDisc_entry.delete(0, END)

def physics():
  global p
  p=Toplevel(d)
  global pDiscussion
  global pDisc_entry
  p.geometry("300x250")
  p.title("PHYSICS")
  Label(p, text = "Type here", bg = "#33C1FF", width = "300", height = "2", font = ("Calibri", 13), pady=True).pack()
  Label(p,text = "").pack()
  pDiscussion=StringVar()
  pDisc_entry = Entry(p, textvariable = pDiscussion)
  pDisc_entry.pack()
  Button(p,text = "Submit",height = "2", width = "30", command = pemail).pack()         ########
  
    
def chemistry():
  global c
  c=Toplevel(d)
  global cDiscussion
  global cDisc_entry
  c.geometry("300x250")
  c.title("CHEMISTRY")
  Label(c, text = "Type here", bg = "#33C1FF", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(c,text = "").pack()
  cDiscussion=StringVar()
  cDisc_entry = Entry(c, textvariable = cDiscussion)
  cDisc_entry.pack()
  Button(c,text = "Submit",height = "2", width = "30", command = cemail).pack()      ########

    
def math():
  global m
  m=Toplevel(d)
  global mDiscussion
  global mDisc_entry
  m.geometry("300x250")
  m.title("MATH")
  Label(m, text = "Type here", bg = "#33C1FF", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(m,text = "").pack()
  mDiscussion=StringVar()
  mDisc_entry = Entry(m, textvariable = mDiscussion)
  mDisc_entry.pack()
  Button(m,text = "Submit",height = "2", width = "30", command = memail).pack()      ########
    
def cs():
  global cs
  cs=Toplevel(d)
  global csDiscussion
  global csDisc_entry
  cs.geometry("300x250")
  cs.title("COMPUTER SCIENCE")
  Label(cs, text = "Type here", bg = "#33C1FF", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(cs,text = "").pack()
  csDiscussion=StringVar()
  csDisc_entry = Entry(cs, textvariable = csDiscussion)
  csDisc_entry.pack()
  Button(cs,text = "Submit",height = "2", width = "30", command = csemail).pack()      ########
    
def english():
  global e
  e=Toplevel(d)
  global eDiscussion
  global eDisc_entry
  e.geometry("300x250")
  e.title("ENGLISH")
  Label(e, text = "Type here", bg = "#33C1FF", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(e,text = "").pack()
  eDiscussion=StringVar()
  eDisc_entry = Entry(e, textvariable = eDiscussion)
  eDisc_entry.pack()
  Button(e,text = "Submit",height = "2", width = "30", command = eemail).pack()      ########    
  
def pemail():
  print(pDiscussion.get())
  server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
  server.login("calibreportal", "calibreportal@2832")
  server.sendmail(
    "calibreportal@gmail.com", 
    "mabel.benjamin@akis.sch.qa.com",
    pDiscussion.get()+"\n\nsent by\n"+ mail)
  server.quit()
  pDisc_entry.delete(0, END)    
def cemail():
  server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
  server.login("calibreportal", "calibreportal@2832")
  server.sendmail(
    "calibreportal@gmail.com", 
    ["vinod.prabhu@akis.sch.qa"],
    cDiscussion.get()+"\n\nsent by\n"+ mail)
  server.quit()
  cDisc_entry.delete(0, END )   
def memail():
  server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
  server.login("calibreportal", "calibreportal@2832")
  server.sendmail(
    "calibreportal@gmail.com", 
    ["mahesh.nair@akis.sch.qa"],
    mDiscussion.get()+"\n\nsent by\n"+ mail)
  server.quit()
  mDisc_entry.delete(0, END)
def csemail():
  server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
  server.login("calibreportal", "calibreportal@2832")
  server.sendmail(
    "calibreportal@gmail.com", 
    ["bharti.patel@akis.sch.qa"],
    csDiscussion.get()+"\n\nsent by\n"+ mail)
  server.quit()
  csDisc_entry.delete(0, END)    
def eemail():
  server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
  server.login("calibreportal", "calibreportal@2832")
  server.sendmail(
    "calibreportal@gmail.com", 
    ["justin.diraviam@akis.sch.qa"],
    eDiscussion.get()+"\n\nsent by\n"+ mail)
  server.quit()
  eDisc_entry.delete(0, END)    
stmain_screen()
#Make sure Inventory application is a function as it needs to be called in this programme.
