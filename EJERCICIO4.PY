def mayor_suma_consecutivos(lista):
    if len(lista) < 2:
        return "La lista debe tener al menos dos números."
    
    mayor_suma = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > mayor_suma:
            mayor_suma = suma_actual
    
    return mayor_suma

entrada = input("Ingrese una lista de números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
resultado = mayor_suma_consecutivos(numeros)

print("La mayor suma entre dos elementos consecutivos es:", resultado)
