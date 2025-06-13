def analizar_matriz_simple():
    print("Ingresa 9 números enteros para la matriz 3x3:")
    matriz = [[int(input(f"[{i+1}][{j+1}]: ")) for j in range(3)] for i in range(3)]

    print("\nMatriz:")
    for fila in matriz:
        print(fila)

    numeros = [n for fila in matriz for n in fila]
    pos = sum(n > 0 for n in numeros)
    neg = sum(n < 0 for n in numeros)
    ceros = sum(n == 0 for n in numeros)

    diag_p = sum(matriz[i][i] for i in range(3))
    diag_s = sum(matriz[i][2 - i] for i in range(3))

    print(f"\nPositivos: {pos}, Negativos: {neg}, Ceros: {ceros}")
    print(f"Diagonal Principal: {diag_p}")
    print(f"Diagonal Secundaria: {diag_s}")

    if diag_p > diag_s:
        print("Diagonal principal es MAYOR.")
    elif diag_p < diag_s:
        print("Diagonal principal es MENOR.")
    else:
        print("Las diagonales son IGUALES.")

if __name__ == "__main__":
    analizar_matriz_simple()
