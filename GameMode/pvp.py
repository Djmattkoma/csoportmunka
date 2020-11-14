
p1nyer = []
p2nyer = []
jatekosok = []

def jatokosmegadas():
    p1 = input("Az 1. játékos neve: ")
    p2 = input("Az 2. játékos neve: ")
    jatekosok.append(p1)
    jatekosok.append(p2)

    print(jatekosok)


def ketjatekos():


    p1kez = input("válasz: kő papír olló: ")
    if p1kez == 1:
        p1kez += "Kő"
    if p1kez == 2:
        p1kez += "Papír"
    if p1kez == 3:
        p1kez += "Olló"
    p2kez = 0


