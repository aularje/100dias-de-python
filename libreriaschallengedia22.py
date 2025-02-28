import random
#uso de librerias
#se importa random
#juego de las adivinanzas

print("Adivina los números entre 1 y 1000!!")
print("++++++++++++++++++++++++++++++++++++")
key = random.randint(1,1000)
#print(key)
intentos = 0
while True:
    adivino = int(input("¿Cuál es tu respuesta?: "))
    if adivino == key:
        print("HAZ GANADO")
        break
    else:
        intentos = intentos + 1
print(f"Te ha tomado {intentos} intentos adivinar el número") 
#fin