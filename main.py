# -------------------------------------------------------
# by : DankBroom228555
# created the 20/09/2022
# main file of : FurastaOS
# -------------------------------------------------------

import dk1 as executable
import file_gestion as files
import help as helpFile

def good_password():
    while True:
        cmd = input("[FurastaOS/admin] >> ")
        if cmd == "ping":
            print("[FurastaOS/info] >> os non connecté à internet")
        elif cmd == "exit" or cmd == "quit":
            print("[FurastaOS/unlogin] >> os arrêté avec succès !")
            break
        elif cmd == "execute":
            print("[FurastaOS/admin/execute/info] >> Entrez le nom du programme à executer")
            executable.start(input("[FurastaOS/dankbroom/execute] >> "))
        elif cmd == "open":
            print("[FurastaOS/info] >> Entrez le nom du fichier à ouvrir")
            files.read(input("[FurastaOS/openFile] >> "))
        elif cmd == "resetWrite":
            print("[FurastaOS/info] >> Entrez le nom du fichier à réinitialiser / réécrire")
            files.reset_write(input("[FurastaOS/resetAndWriteFile] >> "))
        elif cmd == "write":
            print("[FurastaOS/info] >> Entrez le nom du fichier dans lequel écrire")
            files.write(input("[FurastaOS/writeFile] >> "))
        elif cmd == "delete":
            print("[FurastaOS/info] >> Entrez le nom du fichier à supprimer")
            files.delete(input("[FurastaOS/deleteFile] >> "))
        elif cmd == "read":
            print("[FurastaOS/info] >> Entrez le nom du fichier à lire")
            files.read(input("[FurastaOS/readFile] >> "))
        elif cmd == "create":
            print("[FurastaOS/info] >> Entrez le nom du fichier à créer")
            files.create(input("[FurastaOS/createFile] >> "))
        elif cmd == "list" or cmd == "listFiles":
            files.list()
        elif cmd == "help":
            helpFile.help()
        else:
            print("[FurastaOS/dankbroom/error] >> commande inconnue")
