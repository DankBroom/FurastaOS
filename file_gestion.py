# -------------------------------------------------------
# by : DankBroom228555
# created the 21/09/2022
# plugin of : FurastaOS, main.py
# -------------------------------------------------------


import os

def list():
    print("[FurastaOS/list] >> Voici la liste de tout vos fichiers :\n")
    print("\n".join(os.listdir("personalFiles/")))


def delete(file_name):
    if os.path.exists("personalFiles/" + file_name):
        print("[FurastaOS/info] >> êtes vous sûr de vouloir supprimmer le fichier '" + file_name + "' ? ('yes' / 'no')")
        choise = input("[FurastaOS/file/" + file_name + "/delete] >> ")
        if choise == "yes" or choise == "y":
            os.remove("personalFiles/" + file_name)
            print("[FurastaOS/info] >> Le fichier '" + file_name + "' à bien été supprimé !")
        elif choise == "no" or choise == "n":
            print("[FurastaOS/info] >> Commande annulée !")
        else:
            print("[FurastaOS/info] >> Réponse inconnue !")
            print("[FurastaOS/info] >> Commande annulée !")
    else:
        print("[FurastaOS/error] >> Le fichier n'existe pas !")


def create(file_name):
    if os.path.exists("personalFiles/" + file_name):
        print("[FurastaOS/error] >> Le fichier existe déjà !")
    else:
        open("personalFiles/" + file_name,"w+")
        print("[FurastaOS/info] >> Fichier créé avec succès !")

def reset_write(file_name):
    if os.path.exists("personalFiles/" + file_name):
        file = open("personalFiles/" + file_name,"w+")
        file.write("[FurastaOS/file/" + file_name + "] >> " + input("[FurastaOS/file/" + file_name + "/resetAndWrite] >> ") + "\n")
        print("[FurastaOS/info] >> le fichier à bien été réinitialisé et réécrit avec les données rentrées précédement")
    else:
        print("[FurastaOS/info] >> Le fichier n'existe pas, voulez vous le créer ? ('yes' / 'no')")
        choise = input("[FurastaOS/createFile] >> ")
        if choise == "yes" or choise == "y":
            file = open("personalFiles/" + file_name,"w+")
            file.write("[FurastaOS/file/" + file_name + "] >> " + input("[FurastaOS/file/" + file_name + "/resetAndWrite] >> ") + "\n")
        elif choise == "no" or choise == "n":
            print("[FurastaOS/info] >> Commande annulée !")
        else:
            print("[FurastaOS/info] >> Réponse inconnue !")
            print("[FurastaOS/info] >> Commande annulée !")

def write(file_name):
    if os.path.exists("personalFiles/" + file_name):
        file = open("personalFiles/" + file_name,"a+")
        file.write("[FurastaOS/file/" + file_name + "] >> " + input("[FurastaOS/file/" + file_name + "/write] >> ") + "\n")
        print("[FurastaOS/info] >> le fichier à bien été écrit avec les données rentrées précédement")
    else:
        print("[FurastaOS/info] >> Le fichier n'existe pas !")
        print("[FurastaOS/info] >> Commande annulée !")


def read(file_name):
    try:
        os.path.exists(file_name)
        file = open("personalFiles/" + file_name,"r+")
        print(file.read())
    except:
        print("[FurastaOS/info] >> Le fichier n'existe pas !")
        print("[FurastaOS/info] >> Commande annulée !")
