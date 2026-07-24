print("---- simulador de ahorro")
name = input("ingresa tu nombre: ")
monthly_savings = float(input("cuantos dolares ahorras por mes? "))
months = int(input("cuantos meses deseas ahorrar?: "))
total = 0
for month in range(1, months + 1):
    total = total + monthly_savings
    print( f"mes { month}: total acumulado = {total}")
print(f"{name}, en {months} meses abras ahorrado: {total} dolares")