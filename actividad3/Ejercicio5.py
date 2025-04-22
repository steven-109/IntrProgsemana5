litros_mes = float(input("Ingrese la cantidad de litros consumidos en un mes: "))
cant_personas = float(input("Ingrese la cantidad de personas que viven en la casa: "))
 
CONSUMO_MES_PERSO = litros_mes / cant_personas
CONSUMO_DIARIO_PERSO = CONSUMO_MES_PERSO / 30

print(f"El consumo total del mes es de: {litros_mes}")
print(f"La cantidad de personas que viven en la casa es de: {cant_personas}")
print(f"El consumo mensual por persona es de: {CONSUMO_MES_PERSO}")
print(f"El consumo diario por persona es de: {CONSUMO_DIARIO_PERSO}")