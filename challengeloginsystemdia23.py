def login():
    #usuario ingresa su nombre y contraseña
    nombre = input("Ingrese su nombre:")
    contraseña = input("Ingrese su contraseña:")
    #base de datos de claves
    usuario = jesus
    clave = tres3palos
    #comparación
    if nombre == usuario and contraseña == clave:
        print("BIENVENIDO")
        k = 1
    else:
        print("no reconozco el nombre o contraseña, vuelva a intentar")
        k = 0
    return(k)

while True:
    l = login()
    if l == 1:
        break
    else:
        continue
    
