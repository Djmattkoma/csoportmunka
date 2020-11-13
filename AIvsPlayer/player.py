import time

fegyver = {
    0: "kő",
    1: "papír",
    2: "olló"
}


def tipel():
    playertip = input("válasz vegyvert (kő papír olló): ")
    return fegyver.get(playertip, "kő")

def gongol():
    print("A gép gondolkodik: ")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("tejösz")