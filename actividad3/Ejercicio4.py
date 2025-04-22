dista_km = float(input("Ingrese la cantidad recorrida en kilometros: "))
litros_consum = float(input("Ingrese la cantidad de litros consumidos: "))

rendimiento = dista_km/litros_consum
GASTO_TOTAL_COMBUS = litros_consum * 49.01

print(f"La distancia recorrida en kilometros es de: {dista_km}")
print(f"La cantidad de gasolina cosnumida en litros es de: {litros_consum}")
print(f"El rendimiento es de: {rendimiento}")
print(f"El gasto total en combustible es de: {GASTO_TOTAL_COMBUS}")