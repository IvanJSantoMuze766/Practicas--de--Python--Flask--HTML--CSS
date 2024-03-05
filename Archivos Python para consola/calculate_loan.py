def calcular_pago_mensual(monto_prestamo, tasa_interes_anual, plazo_anios):
    """
    Calcula el pago mensual de un préstamo utilizando la fórmula de la hipoteca.
    
    Args:
        monto_prestamo (float): Monto del préstamo.
        tasa_interes_anual (float): Tasa de interés anual en porcentaje.
        plazo_anios (int): Plazo del préstamo en años.
    
    Returns:
        float: El pago mensual del préstamo.
    """
    # Convertir la tasa de interés anual a mensual y el plazo del préstamo a meses
    tasa_interes_mensual = (tasa_interes_anual / 100) / 12
    plazo_meses = plazo_anios * 12
    # Calcular el pago mensual utilizando la fórmula de la hipoteca
    pago_mensual = (monto_prestamo * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -plazo_meses)
    return pago_mensual

def main():
    # Solicitar al usuario los datos del préstamo
    monto_prestamo = float(input("Ingrese el monto del préstamo: "))
    tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
    plazo_anios = int(input("Ingrese el plazo del préstamo en años: "))
    # Calcular el pago mensual del préstamo
    pago_mensual = calcular_pago_mensual(monto_prestamo, tasa_interes_anual, plazo_anios)
    # Imprimir el pago mensual del préstamo
    print(f"El pago mensual del préstamo es: ${pago_mensual:.2f}")

if __name__ == "__main__":
    main()