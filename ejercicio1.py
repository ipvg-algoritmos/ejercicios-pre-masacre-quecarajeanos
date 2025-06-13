def buscar_numero_en_lista():
    lista = [15, 8, 23, 25, 12, 17, 7, 9, 13, 19]
    print(f"Lista: {lista}")

    numero = int(input("¿Qué número deseas buscar? ")) 
    if numero in lista:
        # Mensaje más claro al encontrar el número
        print(f"¡El número {numero} está en la lista! Índice: {lista.index(numero)}")
    else:
        # Mensaje más claro si el número no está
        print(f"El número {numero} no está en la lista.")
            
buscar_numero_en_lista()