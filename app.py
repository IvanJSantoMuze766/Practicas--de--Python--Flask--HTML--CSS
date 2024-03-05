import os
from flask import Flask, render_template, request, session
import random

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configurar una clave secreta para manejar la sesión de usuario
# Esta clave se utiliza para cifrar y descifrar datos de sesión, como cookies
# Si no se proporciona una clave secreta en el entorno, se utiliza una clave predeterminada
app.secret_key = os.environ.get('SECRET_KEY', 'my_default_secret_key')

# Definir la ruta principal '/' que renderiza el archivo HTML principal
@app.route('/')
def index():
    return render_template('index.html')

# Definir la ruta '/calculate_bmi' para manejar el cálculo del IMC enviado desde un formulario POST
@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    # Obtener el peso y la altura del formulario
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    
    # Calcular el índice de masa corporal (IMC)
    bmi = weight / (height ** 2)

    # Clasificar el IMC en categorías de peso y definir el mensaje y el color correspondientes
    if bmi < 18.5:
        category = 'Bajo peso'
        color = 'celeste'  # Color para el mensaje de bajo peso
    elif bmi < 24.9:
        category = 'Peso normal'
        color = 'verde'  # Color para el mensaje de peso normal
    elif bmi < 29.9:
        category = 'Sobrepeso'
        color = 'amarillo'  # Color para el mensaje de sobrepeso
    else:
        category = 'Obeso'
        color = 'rojo'  # Color para el mensaje de obesidad

    # Construir el mensaje del resultado del IMC
    bmi_result = f'Tu IMC es: {bmi:.2f}.'

    # Renderizar el archivo HTML principal con los resultados del IMC
    return render_template('index.html', bmi_result=bmi_result, category=category, color=color)

# Definir la ruta '/check_palindrome' para verificar si una palabra es un palíndromo
@app.route('/check_palindrome', methods=['POST'])
def check_palindrome():
    # Obtener la palabra del formulario y normalizarla
    word = request.form['word'].lower().replace(" ", "")
    
    # Verificar si la palabra es un palíndromo
    palindrome = "¡Es un palíndromo!" if word == word[::-1] else "No es un palíndromo."
    
    # Retornar el resultado como texto para mostrarlo en la página
    return palindrome

# Definir la ruta '/generate_color' para generar un color RGB aleatorio
@app.route('/generate_color', methods=['GET'])
def generate_color():
    # Generar componentes de color rojo, verde y azul aleatorios en el rango de 0 a 255
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # Construir el formato de color RGB
    color = f'rgb({red}, {green}, {blue})'
    
    # Renderizar el archivo HTML principal con el color generado
    return render_template('index.html', color=color)

# Definir la ruta '/calculate_loan' para calcular el pago mensual de un préstamo
@app.route('/calculate_loan', methods=['POST'])
def calculate_loan():
    # Obtener el monto del préstamo, la tasa de interés y el plazo del formulario
    loan_amount = float(request.form['loan_amount'])
    interest_rate = float(request.form['interest_rate']) / 100 / 12
    loan_term = float(request.form['loan_term']) * 12
    
    # Calcular el pago mensual utilizando la fórmula del préstamo
    monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate) ** -loan_term)
    
    # Renderizar el archivo HTML principal con el pago mensual calculado
    return render_template('index.html', monthly_payment=monthly_payment)

# Ejecutar la aplicación Flask en modo de depuración si se ejecuta este script directamente
if __name__ == '__main__':
    app.run(debug=True)