import random
print("Este es un dado con las caras que quieras")
caras = int(input("Cuantas caras quieres que tenga el dado?:"))

def dado(caras):
    lanzamiento = random.randint(1, caras)
    print(f"Haz lanzado el número {lanzamiento}")
    continuar = input("Quiere continuar? S/N:").lower()
    return(continuar)
    
while True:
    dale = dado(caras)
    if dale == "s":
        continue
    else:
        print("Gracias, hasta pronto")
        break
    
    