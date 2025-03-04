#
print("Generador de estadísticas de personajes")
print("++++++++++++++++++++++++++++++++++++++++")
#
def funcionSalud():
    import random
    dado6 = random.randint(1,6)
    dado8 = random.randint(1,8)
    saludj = (str(dado6 * dado8) + "hp")
    return(saludj)

#    
while True:
    guerrero = input("Nombre de tu Guerrero(a):")
    salud = funcionSalud()
    print(f"Su salud es de {salud}")
    cont = input("Continuar? S / N").lower()
    if cont == "s":
        continue
    else:
        print("FIN")
        break
    
    
    