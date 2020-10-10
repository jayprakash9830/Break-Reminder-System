from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Eye Exercise Tutorials")
root.geometry("550x469")
img=Image.open("./image/img1.jpeg")
my_img1=ImageTk.PhotoImage(Image.open("./image/img1.jpeg"))
my_img2=ImageTk.PhotoImage(Image.open("./image/img2.jpeg"))
my_img3=ImageTk.PhotoImage(Image.open("./image/img3.jpeg"))
my_img4=ImageTk.PhotoImage(Image.open("./image/img4.jpeg"))
print(img.size)
image_list=[my_img1,my_img2,my_img3,my_img4]
my_lebel=Label(root,image=my_img1,borderwidth=5)
my_lebel.grid(row=1,column=0,padx=65)
def forward(image_number):
    global my_lebel
    global button_backward
    global button_forward
    my_lebel.grid_forget()
    my_lebel=Label(root,image=image_list[image_number-1])
    
    button_backward=Button(root,text="<<",pady=25,padx=15,borderwidth=2,command=lambda:backward(image_number-1))
    button_forward=Button(root,text=">>",pady=25,padx=15,borderwidth=2,command=lambda:forward(image_number+1))
    if image_number==3:
        button_forward=Button(root,text=">>",pady=25,padx=15,borderwidth=2,state=DISABLED)
    my_lebel.grid(row=1,column=0,padx=65)
    button_forward.place(x=485,y=200)
    button_backward.place(x=5,y=200)

def backward(image_number):
    global my_lebel
    global button_backward
    global button_forward
    my_lebel.grid_forget()
    my_lebel=Label(root,image=image_list[image_number-1])
    
    button_backward=Button(root,text="<<",pady=25,padx=15,borderwidth=2,command=lambda:backward(image_number-1))
    button_forward=Button(root,text=">>",pady=25,padx=15,borderwidth=2,command=lambda:forward(image_number+1))
    if image_number==0:
        button_backward=Button(root,text="<<",pady=25,padx=15,borderwidth=2,state=DISABLED)
    my_lebel.grid(row=1,column=0,padx=65)
    button_forward.place(x=485,y=200)
    button_backward.place(x=5,y=200)

button_backward=Button(root,text="<<",pady=25,padx=15,borderwidth=2,command=lambda:backward(2)).place(x=5,y=200)
button_forward=Button(root,text=">>",pady=25,padx=15,borderwidth=2,command=lambda:forward(2)).place(x=485,y=200)


mainloop()