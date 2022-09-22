from tkinter import*

win= Tk()

win.geometry("750x250")

def close_win(top):
   top.destroy()

def popupwin():
   top= Toplevel(win)
   top.geometry("250x250")

   entry= Entry(top, width= 25)
   entry.pack()
   
   #Create a Button Widget in the Toplevel Window
   button= Button(top, text="Ok", command=lambda:close_win(top))
   button.pack(pady=5, side= TOP)

   
label= Label(win, text="Click the Button to Open the Popup Dialogue", font= ('Helvetica 15 bold'))
label.pack(pady=20)

#Create a Button
button= Button(win, text= "Click Me!", command= popupwin, font= ('Helvetica 14 bold'))
button.pack(pady=20)
win.mainloop()
