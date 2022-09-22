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
    afficher = saisie.get()
    print(afficher)
    fileContent = file.read(afficher)
    print(fileContent)


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
quitBouton.grid(column=0, row=0, padx=5)

# création et affichage du boutton pour lire des fichiers
readBouton = Button( tab2 , text = "Lire", bg = "blue" , fg = "black", command=read)
readBouton.grid(column=0, row=0, padx=5)

# création et affichage du boutton pour supprimer des fichiers
deleteBouton = Button( tab2 , text = "Supprimer", bg = "red" , fg = "black", command=read)
deleteBouton.grid(column=1, row=0, padx=5)

# création et affichage du boutton pour écrire des fichiers
writeBouton = Button( tab2 , text = "Ecrire", bg = "white" , fg = "black", command=read)
writeBouton.grid(column=2, row=0, padx=5)

# création et affichage du boutton pour réécrire des fichiers
resetWriteBouton = Button( tab2 , text = "Réécrire", bg = "black" , fg = "white", command=read)
resetWriteBouton.grid(column=3, row=0, padx=5)

# création et affichage de la zone de texte de nom de fichier
saisie = Entry(tab2)
saisie.grid(column=5, row=0, padx=10)
label = Label(window, text="Bonjour les champions!", font = ( "Arial Bold" , 30 ))
label.grid(column=4, row=0, padx=10)

window.mainloop()
