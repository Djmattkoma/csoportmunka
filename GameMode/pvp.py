
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

    p1kez = 0
    p1kez = input("válasz: kő papír olló: ")
    if gep == 1:
        gepkez += "Kő"
    if gep == 2:
        gepkez += "Papír"
    if gep == 3:
        gepkez += "Olló"
    p2kez = 0


