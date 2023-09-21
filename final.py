from tkinter import *
from tkinter import messagebox
import time
import speech_recognition as sr

root = Tk()
root.geometry("600x660+400+50")
root.resizable(False,False)
root.title("VOICE AUTHENTICATOR")
root.configure(background="#4a4a4a")

def Record():
    file1 = open("password.txt", "r")
    text = file1.read()
    creds = text.split("\n")
    passwd = None
    for i in creds:
        data = i.split(",")
        if data[0] == username.get():
            passwd = data[1]
            break
    if passwd == None:
        messagebox.showinfo("Failed",  "User Not Found")
        return
    print(passwd)
    recognizer=sr.Recognizer()
    t_end = time.time() + 5
    while time.time() <= t_end:
        try:
            with sr.Microphone() as mic:
                #recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic);
                text=recognizer.recognize_google(audio);
                text=text.lower();
                print(text)
                if passwd == text:
                    print(f"Accepted")
                    file1.close()
                    messagebox.showinfo("Success",  "Logged in Successfully")
                    break
                else:
                    print("rejected")
                    messagebox.showinfo("Failed",  "Wrong Password")
            
        except sr.UnknownValueError:
              
             recognizer=sr.Recognizer()
             continue

def setPass():
    global text
    file1 = open("password.txt", "r")
    recognizer=sr.Recognizer()
    t_end = time.time() + 5
    data = file1.read()
    creds = data.split("\n")
    pos = -1
    for i in range(len(creds)):
        data1 = creds[i].split(",")
        if data1[0] == username.get():
            pos = i
    file1.close()
    file1 = open("password.txt", "w")
    while time.time() <= t_end:
        try:
            with sr.Microphone() as mic:
                #recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic);
                text=recognizer.recognize_google(audio);
                text=text.lower();
                if text != None:
                    if pos == -1:
                        if text != None:
                            data += "\n"+username.get()+","+text
                            file1.write(data)
                            messagebox.showinfo("Success", f"User Created your password is {text}")
                    else:
                        data = ""
                        for i in range(len(creds)):
                            data1 = creds[i].split(",")
                            if i == pos:
                                j = data1[0]+","+text+"\n"
                            else:
                                j = creds[i]+"\n"
                            data += j
                        messagebox.showinfo("Success", f"User Updated your password is {text}")
                        file1.write(data)
                    break
                break
        except sr.UnknownValueError:  
             recognizer=sr.Recognizer()
             continue
    
#icon
imagae_icon = PhotoImage(file="Record.png")
root.iconphoto(False,imagae_icon)

#logo
photo=PhotoImage(file="Record.png")
myimage=Label(image=photo,background="#4a4a4a")
myimage.pack(padx=5 ,pady=5)

#name
Label(text="VOICE AUTHENTICATION", font="ariel 30 bold" , background="#4a4a4a" , fg="white" ).pack()

#entry box
username = StringVar()
entry=Entry(root, textvariable=username , font="arial 30" , width=15).pack(pady=10)
Label(text="Enter your username", font="arial 15", background="#4a4a4a" , fg="white").pack()

#button
record=Button(root,font="arial 20" ,text="Login" , bg="#111111" , fg="white" , border=0 , command=Record).pack(pady=20)
setPass=Button(root,font="arial 20" ,text="Create User/Update Pass" , bg="#111111" , fg="white" , border=0 , command=setPass).pack(pady=20)

root.mainloop()