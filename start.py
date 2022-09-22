# -------------------------------------------------------
# by : DankBroom228555
# created the 21/09/2022
# sttart file of : FurastaOS, main.py
# -------------------------------------------------------

# furasta = facile en Gaélique (langue de l'écosse)

import main as OS

def start(name, password):
    if name == "admin":
        if password == "lemotdepasse":
            print("[FurastaOS/dankbroom] >> bonjour " + name)
            OS.good_password()
    else:
        print("[FurastaOS/info] >> Nom d'utilisateur ou mot de passe incorrect")
        inition()


def inition():
    print("[FurastaOS/info] >> Entrez votre nom d'utilisateur")
    login = input("[FurastaOS/Enter_Login] >> ")
    print("[FurastaOS/info] >> Entrez votre mot de passe")
    pw = input("[FurastaOS/Enter_Password] >> ")
    start(login, pw)

inition()
