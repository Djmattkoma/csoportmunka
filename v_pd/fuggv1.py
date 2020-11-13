import random


def fel1():
  gepkez = ""
  emb = 0
  gep = random.randint(1,3)
  if gep == 1:
    gepkez += "Kő"
  if gep == 2:
    gepkez += "Papír"
  if gep == 3:
    gepkez += "Olló"

  embkez = input("Válassz: kő, papír, olló?: ")
  print("A gép keze: ", gepkez)
  print("A te kezed: ", embkez)
  if "k" in embkez:
    emb += 1
  if "p" in embkez:
    emb += 2
  if "l" in embkez:
    emb += 3
  if gep < emb or emb == 1 and gep == 3:
    print("Nyertél!")
  if gep == emb:
    print("Döntetlen!")
  if gep > emb or emb == 3 and gep == 1:
    print("Vesztettél")