def claveGen(numero):
    import random
    pin = ""
    for i in range(numero):
        pin += str(random.randint(0,9))
    return pin
x = int(input(ta,año clave:))
print(claveGen(x))