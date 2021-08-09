def Ordenar(orden):
    orden.sort()
    return orden

def Mayores(DC):
    mayor = 0
    for i in DC:
        if i.get("edad")  >=18:
            mayor = mayor +1
    print("El numero de personas mayores son: ",mayor,"")
    return mayor 
