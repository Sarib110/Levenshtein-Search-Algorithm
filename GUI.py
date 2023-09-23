# ===============  Importing Suitable Libraries ==========================
from tkinter import *                                                   
import tkinter as tk
from PIL import ImageTk, Image
import customtkinter as ctk
import levenstein as lv
#creating main window
def Frame1(bg='black',img = "A.jpeg",xaxis=130,yaxis=300,xsize=1300,ysize=700):
    def toggle_theme():
        if ctk.get_appearance_mode() == 'Dark':
            ctk.set_appearance_mode('light')
            root.destroy()
            Frame1("white","B.jpeg",450,300,500,500)
        else:
            ctk.set_appearance_mode('Dark')
            root.destroy()
            Frame1("black")
    root = ctk.CTkFrame(master=root1,fg_color=bg)
    root.pack(pady=10,padx=40,fill='both',expand=True)
    switch_var = ctk.StringVar(value="on")
    switch_button = ctk.CTkSwitch(root, text="Dark/Light Mode", command=toggle_theme, variable=switch_var, onvalue="on", offvalue="off")
    switch_button.place(x=670,y=50)

    #window icon
    l1 = Label(root,bg="black",width=500,height=2)
    l1.place(x=0, y=0, anchor="nw")

    #apps logo
    apps_logo = ImageTk.PhotoImage(Image.open('apps.jpg'))
    d = Label(root, image = apps_logo,borderwidth=0)
    d.image = apps_logo
    d.place(x=15,y=11)

    # drive logo
    d_logo = ImageTk.PhotoImage(Image.open('Google drive.png'))
    d = Label(root, image = d_logo,borderwidth=0)
    d.image = d_logo
    d.place(x=95,y=11)

    #youtube logo
    yt_logo = ImageTk.PhotoImage(Image.open('youtube.png'))
    y = Label(root, image = yt_logo,borderwidth=0)
    y.image = yt_logo
    y.place(x=170,y=12)
    image = Image.open(img)
    resize_image = image.resize((xsize,ysize))
    yt_logo = ImageTk.PhotoImage(resize_image)
    y = Label(root, image = yt_logo,borderwidth=0)
    y.image = yt_logo
    y.place(x=xaxis,y=yaxis)

    #Gmail logo
    gm_logo = ImageTk.PhotoImage(Image.open('gmail.jpg'))
    l2 = Label(root, image = gm_logo,borderwidth=0)
    l2.image = gm_logo
    l2.place(x=250,y=12)

    G = ctk.CTkLabel(root,text="G",font=("serif typeface",100,'bold'),text_color='blue')
    G.place(x=500,y=180)
    o = ctk.CTkLabel(root,text="o",font=("serif typeface",100,'bold'),text_color='red')
    o.place(x=580,y=180)
    o = ctk.CTkLabel(root,text="o",font=("serif typeface",100,'bold'),text_color='yellow')
    o.place(x=640,y=180)
    g = ctk.CTkLabel(root,text="g",font=("serif typeface",100,'bold'),text_color='blue')
    g.place(x=700,y=180)
    l = ctk.CTkLabel(root,text="l",font=("serif typeface",100,'bold'),text_color='green')
    l.place(x=760,y=180)
    e = ctk.CTkLabel(root,text="e",font=("serif typeface",100,'bold'),text_color='red')
    e.place(x=785,y=180)
    f = ctk.CTkLabel(root,text='🎄',font=("serif typeface",50,'bold'),text_color='green')
    f.place(x=450,y=220)
    f = ctk.CTkLabel(root,text='🎄',font=("serif typeface",50,'bold'),text_color='green')
    f.place(x=840,y=220)
    #search box
    entry = ctk.CTkEntry(master=root,placeholder_text=" 🔎 Google",width=650,height=38)
    entry.place(x=350,y=300)
    def command():
        query1 = entry.get()
        history = lv.Implement(query1)
        Frame(root,history)
    #search button
    search = ctk.CTkButton(master=root,text='Search',command=command)
    search.place(x=600,y=360)
 #*********************************************************************************************
# Create a frame
def Frame(root,label=" "):
    def toggle_theme1():
        if ctk.get_appearance_mode() == 'Dark':
            ctk.set_appearance_mode('light')
            tk_textbox.configure(background="white", foreground="black", highlightbackground="gray")
            switch_button.configure(bg_color="white")
        else:
            ctk.set_appearance_mode('Dark')
            tk_textbox.configure(background="black", foreground="white", highlightbackground="gray")
            switch_button.configure(bg_color="black")
    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=0,padx=0,fill='both',expand=True)
    def command():
        root.destroy()
        Frame1()
    #search button
    search = ctk.CTkButton(master=root,text='⬅',command=command,fg_color='red',font=("Arial",20,"bold"),text_color="black")
    search.place(x=20,y=20)
    tk_textbox = tk.Text(frame, highlightthickness=0)
    tk_textbox.configure(background="black", foreground="white", highlightbackground="gray")
    tk_textbox.pack(fill="both", expand=True, padx=10)
    tk_textbox.configure(font=("Arial", 15), wrap="word")
    # create CTk scrollbar
    ctk_textbox_scrollbar = ctk.CTkScrollbar(frame, command=tk_textbox.yview)
    ctk_textbox_scrollbar.place(relx=1.0, y=0, anchor="ne", relheight=1.0)
    # connect textbox scroll event to CTk scrollbar
    tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)
    switch_var = ctk.StringVar(value="on")
    switch_button = ctk.CTkSwitch(tk_textbox, text="Dark Mode", command=toggle_theme1, variable=switch_var, onvalue="on", offvalue="off")
    switch_button.configure(bg_color="black")
    switch_button.pack(pady=10)
    lines = label.split("\n")
    for line in lines:
        tk_textbox.insert("end", "   " + line + "   \n  ")
root1 = ctk.CTk()
root1.title("Dark/Light Mode")
root1.geometry("1366x768")
ctk.set_appearance_mode('Dark')
Frame1()
root1.mainloop()