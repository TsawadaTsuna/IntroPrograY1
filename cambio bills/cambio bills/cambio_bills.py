print("Programa para calcular cambios")
# Entradas
dinero = int(input("Ingrese el dinero:"))
# Proceso y salida
print(f"Tu cambio son {dinero//200} de 200, {dinero%200//50} de 50, {dinero%200%50//20} de 20, y {dinero%200%50%20} de 1")
