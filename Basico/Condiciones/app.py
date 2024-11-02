calificacion = input("Dame tu calificacion: ")

if calificacion >= 90 and calificacion <= 100:
    print("¡Eres excelente! ¡Felicidades!")
elif calificacion >= 80 and calificacion < 90:
    print("¡Eres bueno! ¡Felicidades!")
elif calificacion >= 70 and calificacion < 80:
    print("¡Puedes mejorar! ¡Animo!")
elif calificacion < 70:
    print("¡Deberías aprender a cocinar! Jajaja")