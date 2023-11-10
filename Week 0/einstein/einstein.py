def get_mass ():
    mass = int(input("m: "))
    print("E:", calc_e(mass))


def calc_e(num):
    return num * (300000000*300000000)

get_mass()