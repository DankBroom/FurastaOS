# -------------------------------------------------------
# by : DankBroom228555
# created the 20/09/2022
# plugin of : FurastaOS, main.py
# -------------------------------------------------------


testPlugValue = False

class plugin():
    def plug(plugin):
        if plugin == "testPlug.frp" and not testPlugValue:
            testPlugValue = True
            return "Pluged !"
        elif plugin == "testPlug.frp" and testPlugValue:
            return "Already pluged !"
        else:
            return "ERROR"