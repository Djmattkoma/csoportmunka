import time

fegyver = {
    0: "kő",
    1: "papír",
    2: "olló"
}

jatekosok = []
p1 = ""
p2 = ""

def nevmegadas():
    p1n = input("1. játékps neve: ")
    p1 = p1n
    p2n = input("2. játékps neve: ")
    p2 = p2n
    jatekosok.append(p1); jatekosok.append(p2)
    print(jatekosok)


def p1tipel():
    print(p1, "játékos jönn")
    player1tip = input(p1 + "választ vegyvert (kő papír olló): ")
    return fegyver.get(player1tip, "kő")

def p2tipel():
    print("2. játékos jönn")
    player2tip = input(p2 + "választ vegyvert (kő papír olló): ")
    return fegyver.get(player2tip, "kő")

def gongol():
    print("A gép gondolkodik: ")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("tejösz")