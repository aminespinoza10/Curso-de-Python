numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

operacion = input("Ingrese la operación a realizar (suma, resta, multiplicacion, division): ")

# Estas son funciones que pueden ser llamadas en cualquier momento
def suma(x, y):
    resultado = x + y
    return 'El resultado de la suma es:' + str(resultado)

def resta(x, y):
    resultado = x - y
    return 'El resultado de la rest es:' + str(resultado)

def multiplicacion(x, y):
    resultado = x * y
    return 'El resultado de la multiplicación es:' + str(resultado)

def division(x, y):
    resultado = x / y
    return 'El resultado de la división es:' + str(resultado)

if operacion == "suma":
    print(suma(numero1, numero2))
elif operacion == "resta":
    print(resta(numero1, numero2))
elif operacion == "multiplicacion":
    print(multiplicacion(numero1, numero2))
elif operacion == "division":
    print(division(numero1, numero2))



