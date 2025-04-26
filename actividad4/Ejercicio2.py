calificacion = int(input("Ingrese la calificacion del estudiante: "))

if calificacion < 60:
    print ("Reprobado")
elif calificacion < 70: 
    print("Regular") 
elif calificacion < 80:
    print ("Bueno")
elif calificacion < 90: 
    print("Muy bueno")
else:
    print("Excelente")    