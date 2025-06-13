def encontrar_mayor_y_menor():
    

    numeros = []
    print("Ingrese números (negativo para finalizar):")

    while True:
        try:
            n = float(input("Número: "))
            if n < 0:
                break
            numeros.append(n)
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

    if numeros:
        print("\nNúmeros ingresados:", numeros)
        print("Mayor:", max(numeros))
        print("Menor:", min(numeros))
    else:
        print("No se ingresaron números válidos.")


if __name__ == "__main__":
    encontrar_mayor_y_menor()
