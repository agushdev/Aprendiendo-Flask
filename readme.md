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