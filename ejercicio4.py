def calcular_promedio_simple():
    numeros = []
    print("Ingresa números. Para terminar, escribe un número negativo.")

    while True:
        try:
            entrada = float(input("Número: "))
            if entrada < 0:
                break
            numeros.append(entrada)
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")

    if numeros:
        print(f"El promedio es: {sum(numeros) / len(numeros):.2f}")
    else:
        print("No ingresaste ningún número.")
        
        #hola profe