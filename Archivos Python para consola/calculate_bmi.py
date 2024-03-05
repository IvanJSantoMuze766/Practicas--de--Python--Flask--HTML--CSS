def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso y la altura.

    Args:
    peso (float): Peso en kilogramos.
    altura (float): Altura en metros.

    Returns:
    float: El IMC calculado.
    """
    return peso / (altura ** 2)

def obtener_categoria_imc(imc):
    """
    Determina la categoría de peso correspondiente al IMC dado.

    Args:
    imc (float): El Índice de Masa Corporal (IMC) calculado.

    Returns:
    str: La categoría de peso.
    """
    if imc < 18.5:
        return 'Bajo peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

def main():
    """
    Función principal para solicitar la entrada del usuario, calcular el IMC y mostrar la categoría de peso.
    """
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    categoria = obtener_categoria_imc(imc)
    print(f"Su IMC es: {imc:.2f}")
    print(f"Categoría de peso: {categoria}")

if __name__ == "__main__":
    main()