def cualTorta(ingrediente, base, cubierta):
    if ingrediente == "chocolate":
        print("La torta de chicolate es increible!!")
    elif ingrediente == "brocoli":
        print("Estás loco?")
    else:
        print("Si, supongo que es bueno...")
    print(f"""Entonces tu quieres una torta de {ingrediente}, con una base de {base} 
    y una cobertura de {cobertura}""")
        
ingre =  input("Cual ingrediente?:")
bas =  input("Cual base?:")
cubi =  input("Cual cubierta?:")
cualTorta(ingre, bas, cubi)