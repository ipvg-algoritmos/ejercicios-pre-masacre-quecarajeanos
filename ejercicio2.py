def contar_vocal_y_consonantes(x):
    vocales = "aeiou"
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    
    contador_vocales = 0
    contador_consonantes = 0
    
    for n in x.lower():
        if n in vocales:
            contador_vocales += 1
        elif n in consonantes:
            contador_consonantes += 1
    
    return contador_vocales, contador_consonantes

if __name__ == "__main__":
    texto_ingresado = input("Ingresa un texto:")
    
    num_vocales, num_consonantes = contar_vocal_y_consonantes(texto_ingresado)
    
    print(f"\nVocales: {num_vocales}")
    print(f"Consonantes: {num_consonantes}")
    