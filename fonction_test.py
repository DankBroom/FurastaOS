# -------------------------------------------------------
# by : DankBroom228555
# created the 20/09/2022
# plugin of : FurastaOS, main.py
# -------------------------------------------------------


def test_mode():
    while True:
        cmd = input("[FurastaOS/TESTMODE] >> ")

        if cmd == "speed":
            a = 0
            while a < 101:
                a = a + 1
                print(a)
        else:
            print("[FurastaOS/TESTMODE/error] >> commande inconnue")
