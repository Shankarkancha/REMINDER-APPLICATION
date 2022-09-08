from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox
from plyer import notification
import time
import smtplib

if __name__=="__main__":
#user details
    GMAIL_ID=""
    PASSWORD=""


    t=Tk()
    t.title("NOTIFIER APP")
    t.geometry("500x300")
    image=Image.open("Icon1.png")
    photo=ImageTk.PhotoImage(image)

    img_label=Label(t,image=photo,padx=1)
    img_label.grid()

    #get details
    def getdetails():
        get_title=title.get()
        get_msg=msg.get()
        get_time=time1.get()
        if get_title=="" or get_time=="" or get_msg=="":
            messagebox.showerror('alert','All fields are required')
        else:
            int_time=int(float(get_time))
            min_to_sec= int_time*60
            messagebox.showinfo("Notifier set","SET NOTIFICATION")
            time.sleep(min_to_sec)
            notification.notify(title=get_title,
                                message=get_msg,
                                app_icon="icon2.ico",
                                app_name="NOTIFIER",
                                timeout=10)
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(GMAIL_ID,PASSWORD)
            server.sendmail("shankarkancha57@gmail.com","nehakancha71@gmail.com",get_msg)
            t.destroy()
        

    #label 1
    t_label=Label(t,text="Title to notify",font=("poppins",10))
    t_label.grid(padx=25,pady=10)

    #Entry 1
    title=Entry(t,width="40",font=("poppins",10))
    title.grid(row=1,column=1,padx=25)

    #label 2
    m_label=Label(t,text="Display Message",font=("poppins",10))
    m_label.grid(pady=10)

    #entry 2
    msg=Entry(t,width="40",font=("poppins",10))
    msg.grid(row=2,column=1)

    #label 3
    time_label=Label(t,text="Set time",font=("poppins",10))
    time_label.grid(pady=10)

    #entry 3
    time1=Entry(t,width="5",font=("poppins",10),justify=LEFT)
    time1.place(x=155,y=174)

    #label 4
    min_label=Label(t,text="MIN",font=("poppins",10))
    min_label.place(x=198,y=173)

    #button
    b1=Button(t,text="SET NOTIFICATION",font=("poppins",10),width=30,background="black",foreground="white",command=getdetails)
    b1.place(x=154,y=220)

    #frame
    f1=Frame(t,bg="grey",relief=SUNKEN)
    f1.place(x=110,y=25)

    #label frame
    frame_label=Label(f1,text="NOTIFIER:APP FOR DESKTOP",font='Helvetica 19 bold')
    frame_label.pack()
    t.mainloop()

