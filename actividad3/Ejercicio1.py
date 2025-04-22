calificacion1 = int(input("Ingrese la primera calificacion :"))
calificacion2 = int(input("Ingrese la segunda calificacion :"))
calificacion3 = int(input("Ingrese la tercera calificacion :"))

suma = calificacion1 + calificacion2 + calificacion3
promedio = suma / 3

print(f"Calificacion 1: {calificacion1:>3}")
print (f"calificacion 2: {calificacion2:>3}")
print(f"calificacion 3 : {calificacion3:>3}")
print (f"promedio : {promedio:.0f}") 
