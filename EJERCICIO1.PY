def operacion_basica(operando1, operando2, operador):
    if operador == "+":
        return operando1 + operando2
    elif operador == "-":
        return operando1 - operando2
    elif operador == "*":
        return operando1 * operando2
    elif operador == "/":
        if operando2 != 0:
            return operando1 / operando2
        else:
            return "Division entre cero no permitida"
    else:
        return " Operador no valido"

resultado = operacion_basica(int(input("ingrese el primer operador")),int(input("ingrese el segundo operador")), input("digite con simbolos (/,*,-,+) la operacion a realizar"))
print(resultado)
