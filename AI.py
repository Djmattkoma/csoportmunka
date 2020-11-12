#ide jönnek a gép dolgai
import random
import time

fegyver = {
    0: "kő",
    1: "papír",
    2: "olló"
}

def gongol():
    print("A gép gondolkodik: ")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("tejösz")

def tipel():
    tip = random.randint(0, 2)
    return fegyver.get(tip, "kő")



