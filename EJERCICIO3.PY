def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista_numeros):
    primos = []
    for numero in lista_numeros:
        if es_primo(numero):
            primos.append(numero)
    return primos

entrada = input("Ingrese una lista de números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
resultado = filtrar_primos(numeros)

print("Los números primos son:", resultado)