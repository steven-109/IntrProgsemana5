cantidad_inicial = int(input("Ingrese la cantidad inicial del inventario:"))
cantidad_recibidos = int(input("Ingrese la cantidad de productos recibidos:"))
cantidad_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))

suma = cantidad_recibidos + cantidad_inicial
inventario_actual = cantidad_vendidos - suma 

print(f"El inventario inicial es de: {cantidad_inicial}")
print(f"La cantidad de productos recibidos es de: {cantidad_recibidos}")
print(f"La cantidad de productos vendidos es de: {cantidad_vendidos}")
print(f"El inventario final disponible es de: {inventario_actual}")