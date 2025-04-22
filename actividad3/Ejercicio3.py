capital_inicial = float(input("Ingrese el capital inicial: "))
interes_anual = float(input("Ingrese la cantidad del interes anual es de:"))
cantidad_años = float(input("Ingrese la cantidad de años es de:"))

porc_dec = interes_anual / 100
calculo = (1 + interes_anual)^cantidad_años
monto_final = calculo * capital_inicial
interes_ganado = capital_inicial - monto_final

print(f"El capital inicial es de: {capital_inicial}")
print(f"La tasa de interes anual es de : {interes_anual}")
print(f"La cantidad de años es de: {cantidad_años}")
print(f"El monto final es de: {monto_final}")
print(f"El interes ganado es de: {interes_ganado}")
