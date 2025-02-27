#Es un juego para seleccionar la operacion matematica y evaluar si el estudiante sabe hacerla
print("JUEGO DE MATEMÁTICA")
print("++++++++++++++++++++")
#Bienvenida
print("Bienvenido a tu juego matemático, aquí demostrarás todo lo aprendido.")
#Nombre
nombre = input("Escribe tu nombre: ")
#Ingresar tipo de operacion
operacion_matematica = input("Indica que tipo de operación llevarás a cabo +, -, *, /:")
#ingresar numero de la tabla 1 al 9
numero_tabla = int(input("Indica el número de tabla que usarás (1 al 9):"))
#comprobar que sabe cada operacion en la tabla elegida
nota = 0
#operacion de suma
if operacion_matematica == "+":
    for i in range(0, 10):
        print(f"{i} + {numero_tabla} = ")
        evaluacion = int(input("Ingresa resultado:"))
        suma = numero_tabla + i
        if evaluacion == suma:
            print("Correcto, continua")
            nota = nota + 1
        else:
            print("Errado, continua")
            nota = nota
#operacion de multiplicacion
elif operacion_matematica == "*":
    for i in range(0, 10):
        print(f"{i} * {numero_tabla} = ")
        evaluacion = int(input("Ingresa resultado:"))
        multiplicacion = numero_tabla * i
        if evaluacion == multiplicacion:
            print("Correcto, continua")
            nota = nota + 1
        else:
            print("Errado, continua")
            nota = nota
#operacion de resta
elif operacion_matematica == "-":
    for i in range(0, 10):
        print(f"{i} - {numero_tabla} = ")
        evaluacion = int(input("Ingresa resultado:"))
        resta = numero_tabla - i
        if evaluacion == resta:
            print("Correcto, continua")
            nota = nota + 1
        else:
            print("Errado, continua")
            nota = nota
#operacion de division
elif operacion_matematica == "/":
    for i in range(0, 10*numero_tabla, numero_tabla):
        print(f"{i} / {numero_tabla} = ")
        evaluacion = float(input("Ingresa resultado:"))
        division = i / numero_tabla
        if evaluacion == division:
            print(">>>Correcto, continua")
            nota = nota + 1
        else:
            print(">>>>>>>>>>>>Errado, continua")
            nota = nota
else:
    print("No es un simbolo válido, FIN")
#dar la calificación obtenida y reconocer el rango aprobado o no
print()
if nota <= 6 and nota >=5:
    print(f"Tu nota es {nota}, aprobaste EN LA RAYA")
elif nota < 8 and nota >=6:
    print(f"Tu nota es {nota}, aprobaste EN EL PROMEDIO")
elif nota <= 9 and nota >=8:
    print(f"Tu nota es {nota}, aprobaste BIEN")
elif nota == 10:
    print(f"Tu nota es {nota}, aprobaste EXCELENTE")
else:
    print(f"Tu nota es {nota}, REPROBASTE")