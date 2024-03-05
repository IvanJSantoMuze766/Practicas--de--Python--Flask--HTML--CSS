def es_palindromo(palabra):
    """
    Comprueba si una palabra es un palíndromo.

    Args:
    palabra (str): La palabra a comprobar.

    Returns:
    bool: True si la palabra es un palíndromo, False de lo contrario.
    """
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    return palabra == palabra[::-1]  # Comprobar si la palabra es igual a su reverso

def main():
    """
    Función principal para solicitar la entrada del usuario y verificar si es un palíndromo.
    """
    palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
    if es_palindromo(palabra):
        print("¡Es un palíndromo!")
    else:
        print("No es un palíndromo.")

if __name__ == "__main__":
    main()