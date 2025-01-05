import calculator

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

operacion = input("Ingrese la operación a realizar (suma, resta, multiplicacion, division): ")

if operacion == "suma":
    print(calculator.suma(numero1, numero2))
elif operacion == "resta":
    print(calculator.resta(numero1, numero2))
elif operacion == "multiplicacion":
    print(calculator.multiplicacion(numero1, numero2))
elif operacion == "division":
    print(calculator.division(numero1, numero2))



