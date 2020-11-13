from AIvsPlayer import player, ai
import  os

def korellenor():
    if ai.tipel() < player.tipel():
        print(ai.gongol())
        print("vesztettel")
    else:
        print(ai.gongol())
        print("nyertél")

    if ai.tipel() == player.tipel():
        print(ai.gongol())
        print("döntettlen")

def tisztito():
    clear = lambda: os.system()
    clear()