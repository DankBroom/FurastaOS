# -------------------------------------------------------
# by : DankBroom228555
# created the 20/09/2022
# plugin of : FurastaOS, main.py
# -------------------------------------------------------

import fonction_test as testmode
import danks as script



def start(file):
    if (file == "boot"):
        print("[DankOS/info/execute/boot] >> Boot file is already started !")
    elif (file == "fonction-test.dk"):
        print("[DankOS/TESTMODE] >> test mode activated")
        testmode.test_mode()
    elif (file == "danks.dk"):
        script.start()
    else:
        print("[DankOS/error] >> ERROR 001")
        print("[DankOS/error] >> The file isn't created")

def other(name):
    return name
