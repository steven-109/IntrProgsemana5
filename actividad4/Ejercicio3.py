a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))

mayor = max(a, b, c)
menor = min(a, b, c)

if a == b == c :
    print("Los numeros son iguales.")
else:     
    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")