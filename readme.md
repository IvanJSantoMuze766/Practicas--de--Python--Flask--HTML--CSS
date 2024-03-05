#**Calculadoras y Funcionalidades**

Este proyecto es una página web que ofrece varias calculadoras y funcionalidades útiles implementadas con Python (usando Flask), HTML y CSS.La idea fue acercarse a lo que hice en otro caso usando JavaScript.

**Funcionalidades**

**Calculadora de IMC (Índice de Masa Corporal)**:

Permite calcular el IMC ingresando el peso (en kilogramos) y la altura (en metros) de una persona.
Muestra el resultado del IMC junto con una categoría de peso correspondiente y un color indicativo.

**Comparador de Palíndromos**:

Permite verificar si una palabra ingresada es un palíndromo (una palabra que se lee igual de izquierda a derecha y de derecha a izquierda).
Muestra un mensaje indicando si la palabra es un palíndromo o no.

**Generador de Colores RGB**:

Genera un color RGB aleatorio cada vez que se presiona el botón "Generar Color".
Muestra el color generado en la página.

**Calculadora de Préstamos**:

Permite calcular el pago mensual de un préstamo ingresando el monto del préstamo, la tasa de interés anual y el plazo del préstamo en años.
Muestra el pago mensual del préstamo calculado.

**Métodos y Funciones Utilizados**:

@app.route('/'): Define la ruta para la página de inicio.

calculate_bmi(): Función para manejar el cálculo del IMC.

check_palindrome(): Función para verificar si una palabra es un palíndromo.

generate_color(): Función para generar un color RGB aleatorio.

calculate_loan(): Función para calcular el pago mensual de un préstamo


**Tecnologías Utilizadas**

-**Python**: Utilizado para el backend del proyecto, especialmente con el framework Flask para crear y manejar las rutas y lógica del servidor web.

-**Flask**: Un framework web de Python que permite construir aplicaciones web de manera rápida y sencilla.

-**HTML**: Utilizado para estructurar y organizar el contenido de la página web.

-**CSS**: Utilizado para aplicar estilos y diseño a la página web, incluyendo colores, fuentes y diseño responsivo.

**Instalación y Uso**

-Clona o descarga el repositorio a tu computadora.

-Instala las dependencias del proyecto utilizando pip install -r requirements.txt.

-Ejecuta la aplicación utilizando el comando python app.py.

-Abre tu navegador web y ve a http://localhost:5000.

-¡Explora y utiliza las diferentes calculadoras y funcionalidades!

**Contribución**
Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, puedes abrir un problema para discutir el cambio que te gustaría realizar o enviar una solicitud de extracción.