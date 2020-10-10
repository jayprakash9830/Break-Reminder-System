from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from time import strftime 
from PIL import ImageTk,Image
# import time
from time import time
import pyttsx3
from datetime import datetime
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import ttk

def exhelp():
    top=Toplevel()
    global my_img1
    global staus
    global button_backward
    global button_forward
    global my_lebel
    my_img1=ImageTk.PhotoImage(Image.open("./image/img1.jpeg"))
    my_img2=ImageTk.PhotoImage(Image.open("./image/img2.jpeg"))
    my_img3=ImageTk.PhotoImage(Image.open("./image/img3.jpeg"))
    my_img4=ImageTk.PhotoImage(Image.open("./image/img4.jpeg"))
    
    
    image_list=[my_img1,my_img2,my_img3,my_img4]


    def forward(image_number):
        global my_lebel
        global button_backward
        global button_forward
        global status
        my_lebel.grid_forget()
        my_lebel=Label(top,image=image_list[image_number-1])
        status=Label(top,text=f"Image {str(image_number+1)} of "+str(len(image_list)),relief=SUNKEN,anchor=E)
        button_backward=Button(top,text="<<",command=lambda:backward(image_number-1))
        button_forward=Button(top,text=">>",command=lambda:forward(image_number+1))
        if image_number==3:
            button_forward=Button(top,text=">>",state=DISABLED)
        my_lebel.grid(row=0,column=1)
        button_backward.grid(row=0,column=0)
        button_forward.grid(row=0,column=2)
        status.grid(row=1,column=0,columnspan=3,sticky=W+E)

    def backward(image_number):
        global my_lebel
        global button_backward
        global button_forward
        global status
        my_lebel.grid_forget()
        my_lebel=Label(top,image=image_list[image_number])
        status=Label(top,text=f"Image {str(image_number+1)} of "+str(len(image_list)),relief=SUNKEN,anchor=E)
        button_backward=Button(top,text="<<",command=lambda:backward(image_number-1))
        button_forward=Button(top,text=">>",command=lambda:forward(image_number+1))
        if image_number==0:
            button_backward=Button(top,text="<<",state=DISABLED)
        my_lebel.grid(row=0,column=1)
        button_backward.grid(row=0,column=0)
        button_forward.grid(row=0,column=2)
        status.grid(row=1,column=0,columnspan=3,sticky=W+E)


    my_lebel=Label(top,image=my_img1,borderwidth=5)
    status=Label(top,text="Image 1 of "+str(len(image_list)),relief=SUNKEN,anchor=E)
    button_forward=Button(top,text=">>",command=lambda:forward(0))
    button_backward=Button(top,text="<<",command=lambda:backward(0))


    button_backward.grid(row=0,column=0)
    button_forward.grid(row=0,column=2)
    my_lebel.grid(row=0,column=1)
    status.grid(row=1,column=0,columnspan=3,sticky=W+E)


def NewFile():
    print("New File!")
def OpenFile():
    name = askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")

def times(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

def popup():
    messagebox.showinfo("Project & Team Infor!!","Healthy Programmer \n Main purpose to remind user about thier health\n\nTeam Member:-\nJay Prakash Sah ->2019202017\nNithyasree ->2019202037\nSubhalaxmi ->2019202055")

    
if __name__ == "__main__":
    init_water=time()
    init_eye=time()
    eye_interval=45
    water_interval=75
    root = Tk()
    root.geometry("350x450")
    root.maxsize(350,450)
    root.title("Break Reminder")
    def log_now(message,name):
        with open("exercise.txt","a+") as f:
            f.write(f"{name} {message} done At {datetime.now()}\n")

    def speek(message):
        engine = pyttsx3.init()
        engine.say(f"Hello Sir it is Your {message} Time")
        engine.runAndWait()
    

    def gettime():
        global init_eye
        global init_water
        if(time()-init_eye>eye_interval):
            speek("Eye Exercise ")
            init_eye=time()
            workComplete=Button(root,text='Work Completed',command=lambda:log_now("Eye work","jay prakash")).place(height=50,width=100,x=50,y=350)
        if(time()-init_water>water_interval):
            speek("Drink Water")
            init_water=time()
            workComplete=Button(root,text="Work Completed",command=lambda:log_now("Drank Water","jay prakash")).place(height=50,width=100,x=50,y=350)
        root.after(1000, gettime)

    def newreminder():

        def newremind(message):
            with open("remind.txt","a+") as f:
                f.write(f"{message.get()} on {cal.selection_get()}\n")
                cal.see(datetime.date(year=2016, month=2, day=5))
            print(message.get(),cal.selection_get())
        newtop = Toplevel(root)
        msg=StringVar()
        import datetime
        today = datetime.date.today()
        mindate = datetime.date(year=2018, month=1, day=21)
        maxdate = today + datetime.timedelta(days=5)
        print(mindate, maxdate)

        cal = Calendar(newtop, font="Arial 14", selectmode='day', locale='en_US',
                       mindate=mindate, maxdate=maxdate, disabledforeground='red',
                       cursor="hand1", year=2018, month=2, day=5)
        cal.grid(row=1,column=0,columnspan=2)

        lable1=Label(newtop,text="Enter Your Message").grid(row=0,column=0)
        receivemessage=Entry(newtop,textvariable=msg,width=35).grid(row=0,column=1)
        

        submit=Button(newtop,text="Submit Reminder",command=lambda:newremind(msg)).grid(row=2,column=1)
      


    menu=Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New Reminder", command=newreminder)
    filemenu.add_command(label="See Upcoming Reminder", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Exercise Tips",command=exhelp)
    helpmenu.add_command(label="About...", command=popup)

    lbl = Label(root, font = ('calibri', 13, 'bold'), 
                background = 'purple', 
                foreground = 'white')
    lbl.place(height=30,width=100,x=240,y=5) 
    times()
    sunday=Checkbutton(root,text="Sunday").place(height=20,width=100,x=100,y=50)
    monday=Checkbutton(root,text="Monday").place(height=20,width=100,x=100,y=75)
    tuesday=Checkbutton(root,text="Tuesday").place(height=20,width=100,x=100,y=100)
    wednesday=Checkbutton(root,text="Wednesday").place(height=20,width=100,x=100,y=125)
    thrusday=Checkbutton(root,text="Thrusday").place(height=20,width=100,x=100,y=150)
    friday=Checkbutton(root,text="Friday").place(height=20,width=100,x=100,y=175)
    saturday=Checkbutton(root,text="Saturday").place(height=20,width=100,x=100,y=200)
    upcoming=Label(root,font=('calibri', 20, 'bold'),text="Upcoming Reminder").place(height=50,width=250,x=50,y=250)
    cstatus=Label(root,font=('calibri',20,'bold'),text="Currest Status").place(height=50,width=250,x=50,y=300)
    workComplete=Button(root,text="Work Completed").place(height=50,width=100,x=50,y=350)
    exit=Button(root,text="Exit",command=root.destroy).place(height=50,width=100,x=200,y=350)
    root.after(1000, gettime)
    root.mainloop()