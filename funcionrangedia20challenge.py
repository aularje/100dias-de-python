print("GENERADOR DE LISTAS")
print("+++++++++++++++++++")
inicio = int(input("Desde: "))
fin = int(input("Hasta: ")) 
incremento = int(input("Incrementos: "))
if inicio > fin:
    incremento = -1 * incremento
else:
    incremento = incremento
print("La lista sería asi: ")
for i in range(inicio, fin, incremento):
    print(i)
    