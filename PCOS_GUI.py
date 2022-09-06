
from tkinter import Tk, Label, Button
import tkinter as tk 
from tkinter import *
import pickle
import numpy as np
from intvalidate import int_validate
from floatvalidate import float_validate
from tkinter import ttk
model = pickle.load(open('log_software.sav', 'rb'))


root = tk.Tk() 
root.title("PCOS Predictor")
root.iconbitmap('C:/Users/Farhan/Desktop/Boss/Thesis/Software/Splash_Screen/icon.ico')
root.configure(bg='#282923')


def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    root.bell()
    return False
    

callback = root.register(only_numeric_input) 

def binary(S):
    if S in ['0', '1','2','3','4','5','6','7','8','9','.']:
        return True
    root.bell() # .bell() plays that ding sound telling you there was invalid input
    return False

callback_binary = (root.register(binary), '%S')

def limitSizeTwo(*args):
    value = Entry1.get()
    if len(value) > 2:
     Entry1.set(value[:2])
     root.bell()
Entry1 = StringVar()
Entry1.trace('w', limitSizeTwo)
 
def limitSizeTwoq(*args):
    value = Entry2.get()
    if len(value) > 2: 
        Entry2.set(value[:2])
        root.bell()
Entry2 = StringVar()
Entry2.trace('w', limitSizeTwoq)

def limitSizefloat(*args):
    value = Entry9.get()
    if len(value) > 5: 
        Entry9.set(value[:5])
        root.bell()

Entry9 = StringVar()
Entry9.trace('w', limitSizefloat)

canvas1 = tk.Canvas(root, width = "750", height = "500")
canvas1.pack()  

frame= tk.Frame(root, bg='#80c1ff')
frame.place(relwidth=1, relheight=1)

label1 = tk.Label(frame, text= 'Follicle No.(R) : ')
label1.config(font=("Times",10), bg='#80c1ff')
label1.place(relx= 0.02, rely=0.05, relwidth= 0.15, relheight= 0.07)
entry1= tk.Entry(frame, width=18, bg="pink", fg="black", borderwidth=3, justify= CENTER, relief= GROOVE)
entry1.config(font=("Times",10),textvariable=Entry1, validate="key", validatecommand=(callback, "%P"))
entry1.place(relx= 0.18, rely=0.05, relwidth= 0.15, relheight= 0.07)
int_validate(entry1, from_=0, to=20)

label2 = tk.Label(frame, text= 'Follicle No.(L) : ')
label2.config(font=("Times",10), bg='#80c1ff')
label2.place(relx= 0.02, rely=0.17, relwidth= 0.15, relheight= 0.07)
entry2= tk.Entry(frame, width=18, bg="pink", fg="black", borderwidth=3, justify= CENTER, relief= GROOVE)
entry2.config(font=("Times",10), textvariable=Entry2, validate="key", validatecommand=(callback, "%P"))
entry2.place(relx= 0.18, rely=0.17, relwidth= 0.15, relheight= 0.07)
int_validate(entry2, from_=0, to=20)

label3 = tk.Label(frame, text= 'Skin Darkening (Y/N) : ')
label3.config(font=("Times",10), bg='#80c1ff')
label3.place(relx= 0.67, rely=0.29, relwidth= 0.16, relheight= 0.07)


label4 = tk.Label(frame, text= 'Hair Growth (Y/N) : ')
label4.config(font=("Times",10), bg='#80c1ff')
label4.place(relx= 0.36, rely=0.05, relwidth= 0.15, relheight= 0.07)

label5 = tk.Label(frame, text= 'Weight Gain (Y/N) : ')
label5.config(font=("Times",10), bg='#80c1ff')
label5.place(relx= 0.36, rely=0.17, relwidth= 0.15, relheight= 0.07)

label6 = tk.Label(frame, text= 'Irregular Cycle (Y/N) : ')
label6.config(font=("Times",10), bg='#80c1ff')
label6.place(relx= 0.35, rely=0.29, relwidth= 0.17, relheight= 0.07)

label7 = tk.Label(frame, text= 'Fast Food (Y/N) : ')
label7.config(font=("Times",10), bg='#80c1ff')
label7.place(relx= 0.67, rely=0.05, relwidth= 0.15, relheight= 0.07)

label8 = tk.Label(frame, text= 'Pimples (Y/N) : ')
label8.config(font=("Times",10), bg='#80c1ff')
label8.place(relx= 0.66, rely=0.17, relwidth= 0.18, relheight= 0.07)

label9 = tk.Label(frame, text= 'AMH(ng/mL) : ')
label9.config(font=("Times",10), bg='#80c1ff')
label9.place(relx= 0.005, rely=0.29, relwidth= 0.18, relheight= 0.07)
entry9= tk.Entry(frame, width=18, bg="pink", fg="black", borderwidth=3, justify= CENTER, relief= GROOVE)
entry9.config(font=("Times",10),textvariable=Entry9, validate='key', vcmd=callback_binary)
entry9.place(relx= 0.18, rely=0.29, relwidth= 0.15, relheight= 0.07)
float_validate(entry9, from_=0, to=80)

global rr
rr=IntVar()
rr.set(2)
button4=Radiobutton(frame, text="Yes", variable=rr, value=1,bg='#80c1ff')
button4.place(relx= 0.84, rely=0.29, relwidth= 0.05, relheight= 0.07)

button5=Radiobutton(frame, text="No", variable=rr, value=0,bg='#80c1ff')
button5.place(relx= 0.90, rely=0.29, relwidth= 0.05, relheight= 0.07)


global rr2
rr2=IntVar()
rr2.set(2)
button6=Radiobutton(frame, text="Yes", variable=rr2, value=1,bg='#80c1ff')
button6.place(relx= 0.53, rely=0.05, relwidth= 0.05, relheight= 0.07)

button7=Radiobutton(frame, text="No", variable=rr2, value=0,bg='#80c1ff')
button7.place(relx= 0.59, rely=0.05, relwidth= 0.05, relheight= 0.07)


global rr3
rr3=IntVar()
rr3.set(2)
button8=Radiobutton(frame, text="Yes", variable=rr3, value=1, bg='#80c1ff')
button8.place(relx= 0.53, rely=0.17, relwidth= 0.05, relheight= 0.07)

button9=Radiobutton(frame, text="No", variable=rr3, value=0, bg='#80c1ff')
button9.place(relx= 0.59, rely=0.17, relwidth= 0.05, relheight= 0.07)



global rr4
rr4=IntVar()
rr4.set(2)
button10=Radiobutton(frame, text="Yes", variable=rr4, value=1, bg='#80c1ff')
button10.place(relx= 0.53, rely=0.29, relwidth= 0.05, relheight= 0.07)

button11=Radiobutton(frame, text="No", variable=rr4, value=0, bg='#80c1ff')
button11.place(relx= 0.59, rely=0.29, relwidth= 0.05, relheight= 0.07)


global rr5
rr5=IntVar()
rr5.set(2)
button12=Radiobutton(frame, text="Yes", variable=rr5, value=1, bg='#80c1ff')
button12.place(relx= 0.84, rely=0.05, relwidth= 0.05, relheight= 0.07)

button13=Radiobutton(frame, text="No", variable=rr5, value=0, bg='#80c1ff')
button13.place(relx= 0.90, rely=0.05, relwidth= 0.05, relheight= 0.07)

global rr6
rr6=IntVar()
rr6.set(2)
button14=Radiobutton(frame, text="Yes", variable=rr6, value=1, bg='#80c1ff')
button14.place(relx= 0.84, rely=0.17, relwidth= 0.05, relheight= 0.07)

button15=Radiobutton(frame, text="No", variable=rr6, value=0, bg='#80c1ff')
button15.place(relx= 0.90, rely=0.17, relwidth= 0.05, relheight= 0.07)


def values():
    New_Follicle_No_R = None
    New_Follicle_No_L = None
    New_AMH = None

    New_Follicle_No_R= entry1.get()
    New_Follicle_No_L= entry2.get()
    New_Skin_Darkening= rr.get()
    New_Hair_Growth= rr2.get()
    New_Weight_Gain= rr3.get()
    New_Irregular_Cycle= rr4.get()
    New_Fast_Food= rr5.get()
    New_Pimples= rr6.get()
    New_AMH= entry9.get()

    if all([New_Follicle_No_R, New_Follicle_No_L, New_AMH]) and 2 not in (New_Skin_Darkening, New_Hair_Growth, New_Weight_Gain , New_Irregular_Cycle , New_Fast_Food , New_Pimples ):

       
        global Prediction_result

        button1['state']=DISABLED


        Prediction_result= (model.predict_proba([[float(New_AMH),New_Weight_Gain,New_Hair_Growth,
                                                                 New_Skin_Darkening,New_Pimples,
                                                                 New_Fast_Food,int(New_Follicle_No_L),int(New_Follicle_No_R),
                                                                 New_Irregular_Cycle]]))


        confidence=Prediction_result[0][1]*100
        first_part,second_part = str(confidence).split('.',2)
        final_result = 'PCOS Probability: ' + first_part + '.' + second_part[:2] + ' %'
        

        global label_Prediction
        global b

        if (confidence<50):
            label_Prediction=tk.Label(frame,text=final_result,bg='Green', fg='white', borderwidth=5, relief= RAISED)
            label_Prediction.config(font=("Times",18))
            label_Prediction.place(relx= 0.32, rely=0.66, relwidth= 0.40, relheight= 0.12)
            b=1
        else:
            label_Prediction=tk.Label(frame,text=final_result,bg='Red', fg='white', borderwidth=5, relief= RAISED)
            label_Prediction.config(font=("Times",18))
            label_Prediction.place(relx= 0.32, rely=0.66, relwidth= 0.40, relheight= 0.12)
            b=1

       
    else: 
        darling="Please Fill Up All The Inputs!"
        label_Prediction=tk.Label(frame,text=darling,bg='#80c1ff', fg='red')
        label_Prediction.config(font=("Times",20))
        label_Prediction.place(relx= 0.29, rely=0.64, relwidth= 0.46, relheight= 0.12)
        b=1
    
def enter1(event):
    button1.config(bg="green", fg="yellow")


def left1(event):
    button1.config(
        bg="#ff99ff",
        fg="red",
    )

def enter2(event):
    button2.config(bg="green", fg="yellow")


def left2(event):
    button2.config(
        bg="yellow",
        fg="red",
    )

def enter3(event):
    button3.config(bg="green", fg="yellow")


def left3(event):
    button3.config(
        bg="yellow",
        fg="red",
    )

button1= tk.Button(frame,text='Predict PCOS',bg='#ff99ff', fg='red',command=values)
button1.config(font=("Times",15),bd=4.5)
button1.place(relx= 0.42, rely=0.48, relwidth= 0.17, relheight= 0.10)

button1.bind("<Enter>", enter1)
button1.bind("<Leave>", left1)  

def result_delete():
    label_Prediction.destroy()
    button1['state']= NORMAL
b=0
def input_delete():
    
    if (b==1):
        label_Prediction.destroy()
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry9.delete(0,'end')
    rr.set(2)
    rr2.set(2)
    rr3.set(2)
    rr4.set(2)
    rr5.set(2)
    rr6.set(2)
    button1['state']= NORMAL
    
 
button2 = Button(frame, width=10, text="Clear Result",bg='yellow', fg='red',command=result_delete)
button2.place(relx= 0.35, rely=0.86, relwidth= 0.16, relheight= 0.07)
button2.config(font=("Times",13),bd=3.5)

button2.bind("<Enter>", enter2)
button2.bind("<Leave>", left2) 

button3 = Button(frame, width=10, text="Clear All",bg='yellow', fg='red',command=input_delete)
button3.place(relx= 0.53, rely=0.86, relwidth= 0.16, relheight= 0.07)
button3.config(font=("Times",13),bd=3.5)

button3.bind("<Enter>", enter3)
button3.bind("<Leave>", left3) 

root.mainloop()






