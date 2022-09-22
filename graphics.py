from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import file_gestion as file


def quitMsgbox():
    quitQuestion = messagebox.askquestion ( 'FurastaOS' , 'Êtes vous sûr de vouloir quitter FurastaOS ?' )
    if quitQuestion == "yes":
        window.destroy()

# lecture des fichiers (affichage dans un label ?)
def read():
    # demande du nom du fichier
    # récupération du nom du fichier
    fileContent = file.read(name)


# création de la fenêtre
window = Tk()
window.title("FurastaOS")
window.geometry ( '750x500' )

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Main')
tab_control.add(tab2, text='FilesGestion')

tab_control.pack(expand=1, fill='both')

# création et affichage du boutton pour quitter
quitBouton = Button( tab1 , text = "Stop FurastaOS", bg = "white" , fg = "black", command=quitMsgbox)
quitBouton.grid(column=0, row=0)

# création et affichage du boutton pour lire des fichiers
readBouton = Button( tab2 , text = "Lire", bg = "blue" , fg = "black", command=read)
readBouton.grid(column=0, row=0)

deleteBouton = Button( tab2 , text = "Supprimer", bg = "red" , fg = "black", command=read)
deleteBouton.grid(column=1, row=0)

writeBouton = Button( tab2 , text = "Ecrire", bg = "white" , fg = "black", command=read)
writeBouton.grid(column=2, row=0)

resetWriteBouton = Button( tab2 , text = "Réécrire", bg = "black" , fg = "white", command=read)
resetWriteBouton.grid(column=3, row=0)

window.mainloop()
