# '{:^30}'.format('centered')
def sor():
    print('{:^30}'.format('**'))


def sor2():
    print('{:^30}'.format('*--*'))


def sor3():
    print('{:^30}'.format('*----*'))


def rajz(vonalsz):
    minta = "*"
    minta += "-"*vonalsz
    minta += "*"
    print('{:^30}'.format(minta))


def vonal(vonsz):
        minta = "-"
        minta += "--" * vonsz
        minta += "-"
        print('{:^30}'.format(minta))


def uniabra(vszam):
    for i in range(vszam):
        rajz(i*2)
    for i in range(vszam,-1,-1):
        rajz(i*2)


def karifa(szam):
    for i in range(szam):
        rajz(i*2)
    vonal(6)