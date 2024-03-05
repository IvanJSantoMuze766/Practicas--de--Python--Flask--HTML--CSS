import random

def generar_color_rgb():
    """
    Genera un color RGB aleatorio.
    
    Returns:
        tuple: Una tupla con los valores de rojo, verde y azul (en ese orden).
    """
    # Generar valores aleatorios para los componentes de color RGB
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

def main():
    # Generar un color RGB aleatorio
    red, green, blue = generar_color_rgb()
    # Imprimir el color generado
    print(f"Color RGB generado: ({red}, {green}, {blue})")

if __name__ == "__main__":
    main()