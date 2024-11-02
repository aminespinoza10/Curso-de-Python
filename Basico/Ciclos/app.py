nombres = ["Amin", "Marcela", "Miranda", "Felipe"]
apellidos = ['Espinoza', 'Martinez', 'Espinoza', 'Bello']
edad = [25, 30, 35, 40]
genero = ['M', 'F', 'F', 'M']

for i in range(len(nombres)):
    if genero[i] == 'M':
        print(f"El nombre es: {nombres[i]} {apellidos[i]}, y su edad es: {edad[i]}, su genero es: Masculino")
    elif genero[i] == 'F':
        print(f"El nombre es: {nombres[i]} {apellidos[i]}, y su edad es: {edad[i]}, su genero es: Femenino")

