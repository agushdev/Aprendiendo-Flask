# <a> **Python - Flask** </a>

##  **Mi apunte de Flask :)**

## <a><u> Que es Flask? </a></u>
### Flask es un micro-framework de Python para desarrollar Web Apps.<br>Es simple y permite a los desarrolladores crear Web Apps rapidamente y con poco codigo.
* ### Proporciona un enrutador URL y herramientas basicas para manejar solicitudes HTTP y respuestas.
* ### Deja al desarrollador la libertad de elegir las bibliotecas y extensiones que mejor se ajusten a sus necesidades.
* ### Ofrece una gran cantidad de flexibilidad y personalizacion. Lo hace adecuado tanto para proyectos chicos como para aplicaciones de gran escala.
* ### Tiene una gran comunidad y documentacion, facilita encontrar soluciones a problemas comunes.

## <a><u> Ventajas de Flask. </a></u>
* ### Simplicidad.
* ### Flexibilidad.
* ### Pequeño y ligero.
* ### Facil de integrar con otros servicios.
* ### Comunidad activa.


## <a><u> Como empezar? </a></u>
### Para empezar con el proyecto, debemos de crear el entorno virtual de este.

## <a><u> Que es un entorno virtual y por que lo utilizamos? </u></a>
### Un entorno virtual es una herramienta que permite aislar las dependencias y paquetes de un proyecto especifico.
### Basicamente te sirve para para evitar conflictos entre diferentes proyectos que podrian utilizar distintas versiones de estas dependencias o paquetes.
### Al usar un entorno para cada proyecto, no se interfieren las versiones especificas de cada biblioteca.

## <a><u> Como crear y activar un entorno virtual? </a></u>
### Trabajamos con el cmd, vamos a la carpeta del proyecto con ``cd ./carpeta``.<br>Creamos el entorno con: ``py -3 -m venv nombre_entorno``<br>Casi siempre se le nombra simplemente env.
### Una vez creado, se activa con ``.\nombre_entorno\Scripts\activate``, y se desactiva con ``deactivate``.

## <a><u> Instalamos Flask. </a></u>
### Instalamos flask con ``pip install Flask``, y checkeamos con ``pip list`` para checkear si se instalo correctamente.

## <a><u> Abrimos Visual con el entorno. </a></u>
### Con el entorno activado abrimos el Visual con ``code .``.<br>Esto te ahorra trabajo y te abre el proyecto con el entorno.

---

## <a><u> Creamos el modulo principal </a></u>
### Importamos flask y lo que utilicemos: ``from flask import Flask``.
### Creamos la app: ``app = Flask(__name__)``<br>El argumento ``__name__`` toma el nombre del modulo principal.
### Agregamos las vistas/rutas que queramos con decoradores:<br>``@app.route('/')``. "/" es la ruta principal, ponemos la que necesitemos.

````py
@app.route('/')
def index():
    return 'Pagina principal'

@app.route('/saludo')
def hello():
    return 'Hola!'
````
### Una app minima nos quedaria:
````py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
````

## <a><u> Como ejecutar la app? </a></u>
### Desde la terminal(cmd) y dentro del entorno.<br>Ejecutamos la app con: ``flask --app modulo_principal run --reload``<br>Reload: reinicia cada vez que se hace un cambio.
### Esto te da un link de host local para visualizar la aplicacion.
### Si queremos usar el modo debug solo agregamos ``--debug`` al final en la ejecucion de la app. ``flask --app modulo_principal run --debug``

## <a><u> Uso de variables en rutas: </a></u>
### Si requerimos de una ruta especifica del valor de una variable, podemos utilizar:
````py
@app.route('/user/<converter:variable>')
def show_user_profile(variable):
    return f'Hola {variable}'
````
### Ponemos la variable con su tipo de dato en la ruta entre <> y la utilizamos de parametro en la funcion.
### <u>Los tipos de datos son los siguientes</u>:
* ### string: (default) acepta cualquier texto sin barra diagonal
* ### int: acepta enteros positivos
* ### float: acepta valores positivos de coma flotante
* ### path: lo mismo que string pero acepta barras diagonales
* ### uuid: acepta cadenas UUID

## <a><u> Escape de HTML: </a></u>
### En Flask se recomienda escapar todas las entradas de usuario por <i>seguridad</i>.<br>Esto puede evitar ataques de inyecciones.
### Desde markupsafe solo importamos escape, esto ya deberia de estar instalado por flask. Se puede usar en el entorno pip list para comprobar.

````py
from markupsafe import escape

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
````

## <a><u> Plantillas con Jinja y HTML: </a></u>
## Introduccion a plantillas:
### Jinja2 es un motor de plantillas para Python que permite crear plantillas dinamicas y generar contenido HTML (o otros tipos de documentos).<br> Con datos en tiempo de ejecucion.
### Tambien se pueden utilizar estructuras de control en Jinja2 como bucles y condicionales para crear contenido dinamico en base a datos en tiempo de ejecucion.
### Jinja2 se utiliza principalmente con Flask, pero puede utilizarse independientemente o con otros frameworks web de Python.

## Creacion de plantillas:
### Primero creamos una carpeta dentro del proyecto que se llame 'templates'.<br>Dentro de esta carpeta creamos nuestras plantillas. Por ej un <i>index.html</i>:
````html
<!DOCTYPE html>
<html>
    <head>
        <title> Mi sitio Web </title>
    </head>
    <body>
        <h1> Bienvenido a mi sitio Web </h1>
    </body>
</html>
````
### Para renderizar una plantilla con Flask, utilizamos una funcion que importamos desde el modulo flask: ``from flask import Flask, render_template``.
### Implementamos la plantilla en el modulo principal.<br>Para esto utilizamos la funcion ``render-template('documento')``:
````py
@app.route('/index')
def index():
    return render-template('index.html')
````
### Si queremos enviar una variable agregamos otro argumento nombre_variable=variable.
````py
@app.route('/index')
def index():
    variable = 'Agu'
    return render-template('index.html', name = variable)
````
### Y ya podriamos usar esa variable en el index.html con ``{{name}}``.<br>Para usar estructuras de control utilizamos ``{%  %}``, en el medio va la estructura de control por ej:
````html
<!DOCTYPE html>
<html>
    <head>
        <title> Mi sitio Web </title>
    </head>
    <body>
        <h1> Bienvenido a mi sitio Web </h1>
        {% if name %}
        <p> Hola, {{name}} </p>
        {% else %}
        <p> Hola, desconocido </p>
        {% endif %}
    </body>
</html>
````
### Hay que aclarar el final de la estructura de control por ej en un if: ``endif``.

## <a><u> Uso de variables y bucles: </a></u>
### Tambien podemos enviar listas y iterar cada elemento con un for.
````py
    def index()
    friends=['Alexander','Roel','Juan','Pedro']
    return render-template('index.html', friends=friends)
````

````html
<!DOCTYPE html>
<html>
    <head>
        <title> Mi sitio Web </title>
    </head>
    <body>
        <h2> Lista de amigos </h2>
        <ul>
            {% for friend in friends %}
            <li> {{friend}} </li>
            {% endfor %}
        </ul>
    </body>
</html>
````
## <a><u> Uso de herencia y plantillas: </a></u>
## Que es la herencia?
### La herencia de plantillas en Flask es una caracteristica que permite crear una estructura de plantillas base y extenderlas en otras plantillas.<br>Esto facilita la reutilización de código y mantiene una estructura consistente en todas las páginas de una aplicación web.
## Como funciona esta herencia?
### La herencia de plantillas permite definir una plantilla base que contiene elementos comunes (como el encabezado, el pie de página, y la navegación) y luego definir plantillas secundarias que heredan de esta base y agregan o sobrescriben contenido específico.

## Pasos para Utilizar la Herencia de Plantillas en Flask
### 1- Crear plantilla base:<br>La plantilla base contiene el diseño general y las partes comunes de las páginas. Utiliza bloques de contenido que pueden ser sobrescritos por plantillas secundarias.

````html
<!DOCTYPE html>
<html>
    <head>
        <title> Mi sitio Web - {% block title %}{% endblock %} </title>
    </head>
    <body>
        {% block content %}
        <!-- Bloque de contenido -->
        {% endblock %}
    </body>
</html>
````
### 2- Crear plantilla secundaria:<br>Las plantillas secundarias heredan de la plantilla base y pueden sobrescribir o agregar contenido a los bloques definidos en la plantilla base.
````html
{% extends 'base.html' %}
{% block title %} Pagina de inicio {% endblock %}

{% block content%}
    <h2> Lista de amigos </h2>
        <ul>
            {% for friend in friends %}
            <li> {{friend}} </li>
            {% endfor %}
        </ul>
{% endblock %}

    </body>
</html>
````
### 3- Renderizar la Plantilla desde Flask:<br> En tu aplicación Flask, renderiza la plantilla secundaria en tus rutas.
````py
@app.route('/')
def home():
    return render_template('index.html')
````
## Usos de filtros y funciones:
### Las variables pueden ser modificadas por filtros.<br>Los filtros estan separados de la variable por el simbolo '|' y pueden tener argumentos opcionales en parentesis.<br>Se pueden encadenar varios filtros.
### Por ej:
````py
{% block content %}
    <p> Hola, {{ name | upper }}!</p>

    <ul>
        {% for friend in friends | reverse %}
            <li> {{ friend }} </li>
        {% endfor %}
    </ul>
{% endblock %}
````

## <a><u >Como enviar datos a las plantillas? </a></u>
### Los envias en forma de dict con la funcion: <br>``render_template('vista.documento', parametro)``.
1. ### Defino una funcion de vista:
    * #### La funcion ``home()`` en ``app.py`` define los<br>datos del usuario en un diccionario llamado ``user``.


2. ### Renderizo la plantilla con ``render_template()``:
    * #### ``render_template('index.html', user=user)``<br>pasa el diccionario user a la plantilla index.html.

````py
@app.route('/')
def home():
    user = {
        'username': 'Jane Doe',
        'age': 30,
        'hobbies': ['Reading', 'Cycling', 'Photography']
    }
    return render_template('index.html', user=user)
````
3. ### Accedo a las variables en la plantilla templates/index.html:<br>
    * #### En ``index.html``, se accede a las propiedades<br>del objeto ``user`` usando la sintaxis de Jinja2 ``{{ user.property }}``.
    * #### El bucle ``for`` de Jinja2 lo uso para iterar sobre la lista<br>de hobbies y mostrarlos en una lista HTML.
````py
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title> Perfil de Usuario </title>
</head>
<body>
    <h1> Bienvenido, {{ user.username }}! </h1>
    <p> Edad: {{ user.age }} </p>
    <h2> Hobbies: </h2>
    <ul>
        {% for hobby in user.hobbies %}
            <li> {{ hobby }} </li>
        {% endfor %}
    </ul>
</body>
</html>
````
## Beneficios de esta funcion:
* ### Dinamicidad: Permite crear contenido dinamico basado de datos pasados desde el backend.
* ### Reutilizacion: Facilita la reutilizacion de plantillas con diferentes datos.

## <a><u >Enlaces y rutas: </a></u>
## Constructor URL:
### La funcion: ``url_for()`` sirve para generar URLs dinamicamente.
### En lugar de escribir las URLs de forma manual y estática, ``url_for()`` permite crear URLs basadas en el nombre de la función de vista y los parametros asociados.

## Por que es mejor utilizar la funcion url_for()?
1. ### Mantenimiento simplificado:
    * Si cambias la ruta de una vista en tu app, solo necesitas<br>actualizar la ruta en un lugar (en la funcion de vista), y <br>``url_for()`` generara automaticamente las URLs<br>correctas en todo tu proyecto.
2. ### Evita errores:
    * Ayuda a evitar errores tipograficos en las URLs.<br>Al usar el nombre de la funcion en lugar de una<br>cadena de texto con la URL, reduces la probabilidad<br>de errores.
3. ### Gestion de parametros:
    * Facilita la gestion de parametros de URL.<br>``url_for()`` puede aceptar parametros adicionales<br>que se incluiran en la URL generada.
4. ### Mayor flexibilidad:
    * Permite generar URLs absolutas y anclar URLs<br>relativas automaticamente.

## Como se utiliza?
### Se importa la funcion desde ``from flask import Flask, url_for``.<br>Y se utiliza la funcion url_for('vista', parametro='valor_parametro').
````py
@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('code', code = 'print ("Hola")'))

@app.route('/code/<path:code>')
def code(code):
    return f'<code> {{ escape(code) }} </code>'
````
## Uso en plantillas:

### ``url_for()`` es util en plantillas Jinja2. <br>Por ej, para crear un enlace en una plantilla HTML:
````html
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Inicio</title>
</head>
<body>
    <nav>
        <ul>
            <li> <a href="{url_for('index')}"> Inicio </a></li>
            <li> <a href="{url_for('code', code = 'print(code)' )}"> Code </a></li>
        </ul>
    </nav>
</body>
</html>
````

## <a><u> Integrar archivos estaticos (css y js): </a></u>
### Para organizarnos bien creamos una carpeta y la llamamos ``static``.<br>Dentro de esta creamos otras carpetas segun lo que necesitemos.<br>Como por ej: css, img, js.

## CSS:
### Si trabajamos con css, en la carpeta ``/static/css`` creamos un archivo ``style.css``.<br>Ejemplo:
````css
body{
    font-family: sans-serif;
    background-color: #ccc;
}

h1{
    color: brown;
}
````
### Linkeamos en la plantilla que queramos, en el head con ``url_for()``.
````html
<!DOCTYPE html>
<html>
    <head>
        <title> Ejemplo link css </title>
        <link rel"stylesheet" href="{{url_for('static'),filename='css/style.css'}}">
    </head>
    <body>
        <!-- Todo el body -->
    </body>
</html>
````
## JS:
### Lo mismo en la carpeta ``static/js`` creamos un archivo ``main.js``.
````js
    console.log('Hola Mundo')
````
### Linkeo en la plantilla que queramos, en lo ultimo del body con ``url_for()``.
````html
<!DOCTYPE html>
<html>
    <head>
        <title> Ejemplo link js </title>
    </head>
    <body>
        <script src="{{ url_for('static'), filename = 'js/main.js' }}"> </script>
    </body>
</html>
````

## <a><u> Manejo de formularios: </a></u>

## Que son los formularios?
### Los formularios son una parte importante de cualquier app web.<br>Permiten recibir y enviar informacion del usuario.

## Como se crean?
### En Flask, los formularios se pueden crear usando HTML y CSS, pero tambien existen bibliotecas que facilitan el proceso y añaden caracteristicas adicionales como la validacion de datos y la proteccion contra ataques.
### Los formularios son importantes en Flask, porque te permiten interactuar con el usuario de manera mas efectiva.
### Por ejemplo:
* ### Formularios de inicio de sesion: Para que los usuarios puedan loguearse en tu app.
* ### Formularios de registro: Para que los usuarios puedan crear su cuenta.
* ### Formularios de busqueda: Para que los usuarios puedan buscar informacion en tu app.
* ### Y muchisimos mas.

## Formulario login y register (metodos y request):
### Creamos una carpeta auth ubicada en ``templates/auth``, donde vamos a ubicar la pagina de register y login.
### Renderizo plantilla en la ruta ``/auth/register``, y trabajo con metodos.<br>Con el metodo ``GET`` solicito los datos al servidor y con ``POST`` los envio.
````py
@app.route('/auth/register', methods = ['GET', 'POST'])
def register()
    return render_template('auth/register.html')
````

## Creacion de formularios:
### Dentro de una plantilla (usemos de ejemplo la pagina de registro).<br>En este caso ``register.html``, creamos el formulario con:
````html
<form action="" method="post">
    <label for="username"> Nombre de usuario </label>
    <input type="text" name="username" id="username" required>
    <br>
    <label for="password"> Contrasenia </label>
    <input type="password" name="password" id="password" required>
    <br>
    <input type="submit" value="Registrar">
</form>
````
> El metodo post sirve para cuando envias los datos con el submit, que no se vea todo en la URL.

## Obtener esos datos del formulario:

### Ahora necesitamos obtener esos datos, para eso vamos a utilizar el objeto request.<br>Importamos junto con Flask ``from flask import Flask, request``.
### El objeto request captura la peticion del cliente mediante el formulario.
````py
from flask import Flask, request

# ...

@app.route('/auth/register', methods = ['GET', 'POST'])
def register()
    if request.method == 'POST'
        username = request.form['username']
        password = request.form['password']
        return f"Nombre de usuario: {username}, Contrasenia: {password}"
    return render_template('auth/register.html')
````

## Validar los datos del formulario:

````py
from flask import Flask, request

# ...

@app.route('/auth/register', methods = ['GET', 'POST'])
def register()
    if request.method == 'POST'
        username = request.form['username']
        password = request.form['password']

        if len(username) >= 4 and len(username) <= 25 and 
        len(password) >= 6 and len(password) <= 40:
            return f"Nombre de usuario: {username}, Contrasenia: {password}"
        else:
            error= """"Nombre de usuario debe tener entre 4 y 25 caracteres y
            la contrasenia debe tener entre 6 y 40 caracteres.
            """"
            return render_template('auth/register.html', error= error)
    return render_template('auth/register.html')
````

````html
<form action="" method="post">
    <label for="username"> Nombre de usuario </label>
    <input type="text" name="username" id="username" required>
    <br>
    <label for="password"> Contrasenia </label>
    <input type="password" name="password" id="password" required>
    <br>
    <input type="submit" value="Registrar">
</form>

{% if error %}
    <p style="color: red;">{{ error }}</p>
{% endif %}
````

## <a></u> Formulario con WTForms: </a></u>

## Que es WTForms?
### WTForms es una biblioteca de Python que facilita la creacion y validacion de formularios web.<br>Puede usarse de manera independiente, pero es comun utilizarla con Flask por la extension FLASK-WTF.

## Instalamos WTForms
### Lo instalamos desde el entorno del proyecto con ``pip install flask-wtf``.

## Crear formulario con WTForms:
### Primero necesitamos importar el modulo ``from flask_wtf import FlaskForm``.<br>Y el modulo ``from wtforms import StringField, PasswordField, SubmitField``.
### FlaskForm es para crear los formularios. Los campos/field son para crear inputs.

````py
class RegisterForm(FlaskForm):
    username= StringField("Nombre de usuario: ")
    password= PasswordField("Contrasenia: ")
    submit= SubmitField("Registrar: ")

# ...

@app.route('/auth/register', methods = ['GET', 'POST'])
def register()
    form= RegisterForm()
    if form.validate_on_submit():
        username= form.username.data
        password= form.password.data
        return f"Nombre de usuario: {username}, Contrasenia: {password}"
    return render_template('auth/register.html', form= form)
````

````html
<form action="" method="post">
    {{ form.hidden_tag }}
    {{ form.username.label }} {{ form.username }}
    {{ form.password.label }} {{ form.password }}
    {{ form.submit.label }} {{ form.submit }}
</form>
````
### Necesitamos crear una clave secreta (secret key).

````py
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)
````

## Validar datos con WTForm:
### Necesitamos importar ``from wtforms.validators import DataRequired, Length
### DataRequired: dato requerido si o si para validar.<br>Length: requiere que cumpla la condicion de tantas letras para validar.
