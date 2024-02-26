import socket
from tkinter import * 
from threading import Thread
import random 
import time
from tkinter import ttk
server=None 
port=None
ip_address=None
clients={}
nameWindow=None
EnterName=None
EnterPlace=None
EnterName2=None
ChatWindow_1=None
ChatWindow=None
bottomEntry=None
filePath=None




def a():
    global server,nameWindow,EnterName,EnterPlace,EnterName2,ChatWindow_1,ChatWindow,bottomEntry,filePath
    nameWindow=Tk()
    nameWindow.title("Messenger")
    nameWindow.geometry("750x600") 
    EnterName=Label(nameWindow,text="Enter Your Name:",font=("Arial",12))
    EnterName.place(relx=.1,rely=.1)
    EnterPlace=Entry(nameWindow,bg="white",text="",bd=2,font=("Arial",12))
    EnterPlace.place(relx=.40,rely=.1)
    EnterButton=Button(nameWindow,bg="gray",text="Connect To Chat Server",font=("Arial",12),bd=3)
    EnterButton.place(relx=.70,rely=.1)
    seperator=ttk.Separator(nameWindow,orient="horizontal")
    seperator.place(relx=.15,rely=.2084545456646347346346437835356673664367736436,relwidth=1,)
    EnterName2=Label(nameWindow,text="Active Users:",font=("Arial",12))
    EnterName2.place(relx=.1,rely=.25)
    EnterPlace=Listbox(nameWindow,bg="white",bd=2,height=5,width=100,font=("Arial",12))
    EnterPlace.place(relx=.1,rely=.3)
    scroll=Scrollbar(EnterPlace)
    scroll.place(relheight=1.00000000000000000000000000000000000000000000000000000000000000000,relx=.73449324823943717432740123471273412936192317291754454858458047540743545303753043756465)
    scroll.config(command=EnterPlace.yview)
    ConnectButton=Button(nameWindow,bg="gray",text="Connect",font=("Arial",12),bd=3)
    ConnectButton.place(relx=.54,rely=.5)
    DisconnectButton=Button(nameWindow,bg="gray",text="Disconnect",font=("Arial",12),bd=3)
    DisconnectButton.place(relx=.65,rely=.5)
    RefreshButton=Button(nameWindow,bg="gray",text="Refresh",font=("Arial",12),bd=3)
    RefreshButton.place(relx=.78,rely=.5)
    ChatWindow_l=Label(nameWindow,text="Chat Window",font=("Arial",12))
    ChatWindow_l.place(relx=.1,rely=.6)
    ChatWindow=Text(nameWindow,bg="white",bd=2,height=5,width=100,font=("Arial",12))
    ChatWindow.place(relx=.1,rely=.64)
    scroll=Scrollbar(ChatWindow)
    scroll.place(relheight=1.00000000000000000000000000000000000000000000000000000000000000000,relx=.73449324823943717432740123471273412936192317291754454858458047540743545303753043756465)
    scroll.config(command=ChatWindow.yview)
    attachButton=Button(nameWindow,bg="gray",text="Attach & Send",font=("Arial",12),bd=3)
    attachButton.place(relx=.1,rely=.82)
    BottomEntry=Entry(nameWindow,bg="gray",text="",width=45,font=("Arial",12),bd=3)
    BottomEntry.place(relx=.3,rely=.82)
    sendButton=Button(nameWindow,bg="gray",text="Send",font=("Arial",12),bd=3)
    sendButton.place(relx=.9,rely=.82)

    filePath=Label(nameWindow,text="PATH OF FILE",font=("Arial",12),bg="cyan",fg="white")
    filePath.place(relx=.1,rely=.91)
    

    nameWindow.mainloop()
    

    

a()