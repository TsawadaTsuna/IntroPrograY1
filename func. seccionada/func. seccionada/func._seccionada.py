n = float(input("ingrese un entesro:"))
if n <= -1:
    print(f"Resultado: {2*n}")
elif n > -1 and n < 1:
    print(f"Resultado: {2*n+1}")
elif n >= 1 and n < 4:
    print(f"Resultado: {-n+4}")
else:
    print(f"Resultado: {n-1}")