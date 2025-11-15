<style>
    /* Tipografía general */
    * {
        font-family: "Courier New", Courier, monospace;
        line-height: 1.5;
    }

    /* Estilos de títulos */
    h1, h2, h3, h4 {
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    h1 {
        font-size: 32px;
        border-left: 20px solid rgb(25, 75, 50);
        border-bottom: 20px solid rgb(25, 75, 50);
        padding-bottom: 8px;
        padding-left: 25px;
    }

    h2 {
        font-size: 26px !important;
        padding: 20px;
        margin-top: 85px !important;
        margin-bottom: 0px !important;
        border-left: 12px solid rgb(54, 115, 85);
        border-top: 5px solid rgb(54, 115, 85);

        background: rgb(25, 75, 50);
    }

    h3 {
        font-size: 18px !important;
        padding: 10px;
        margin-top: 30px !important;
        margin-bottom: 0px !important;
        border-left: 24px solid rgb(54, 108, 115);
        background: rgb(25, 49, 75);
        align-items: center;
        align-content: center;
        vertical-align: middle;
        text-align: center;
    }

    h4 {
        font-size: 14px !important;
        padding: 10px;
        margin-top: 30px !important;
        margin-bottom: 0px !important;
        border-left: 24px solid rgb(115, 110, 54);
        background: rgb(75, 53, 25);
        align-items: center;
        align-content: center;
        vertical-align: middle;
        text-align: center;
    }

    p {
        margin-top: 20px !important;
    }

    /* Estilos de links */
    a {
        color: rgb(57, 156, 107) !important; /* Python dark blue */
        text-decoration: none !important;
        font-weight: 800;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Estilo para listas */
    ul, ol {
        margin-left: 20px;
    }

    /* Tablas */
    table {
        border-collapse: collapse;
        margin: 10px 0;
    }

    table, th, td {
        border: 1px solid #999;
    }

    th, td {
        padding: 6px 12px;
    }

    .finger {
        animation: float 0.5s ease-in-out infinite alternate;
    }

    @keyframes float {
        from {
            transform: translateY(0);
        }
        to {
            transform: translateY(30px);
        }
    }
</style>

<h1 style="font-size:3rem;">
    Introducción a
  <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.djangoproject.com%2Fimg%2Flogos%2Fdjango-logo-negative.1d528e2cb5fb.png&f=1&nofb=1&ipt=c8d83bb130dd9b7fed5e3cf716f92a76ef41a80ec967a5382230e260c10a5b06" width="150" style="vertical-align: middle; margin-left: 5px; background-color:rgba(3, 18, 11, 0.36); padding: 5px 5px; border-radius: 20px;">
</h1>

Guía de introducción a <a href="https://docs.djangoproject.com/es/5.2/">Django (Python)</a>. Incluye entorno virtual, instalación, estructura del proyecto, apps, rutas, modelos, vistas, templates, migraciones, panel admin, ORM y template tags.

<center>
    <img class="finger" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhotemoji.com%2Fimages%2Femoji%2Fl%2F17zcrtb11cx2zl.png&f=1&nofb=1&ipt=98be3384ba263dd958fd6f0e1e62f492e7fe0b72366391dede7d2d354b3a3cbe" width="60">
</center>

## 1. Crear entorno de trabajo

###  Crear carpeta del proyecto

```bash
mkdir primerproyecto
cd primerproyecto
```


###  Crear y activar entorno virtual

```bash
python3 -m venv env
source env/bin/activate
```

Para salir:

```bash
deactivate
```



## 2. Instalación de Django

###  Crear archivo `requirements.txt`

Contenido:

```
Django==5.1.3
```

###  Instalar dependencias

```bash
pip install -r requirements.txt
```

###  Verificar instalación

```bash
django-admin --version
```



## 3. Crear proyecto y aplicación

###  Crear proyecto (IMPORTANTE: el punto al final)

```bash
django-admin startproject nombre_proyecto .
```

###  Crear una aplicación

```bash
python manage.py startapp nombre_aplicacion
```



## 4. Configuración inicial (`settings.py`)

Ajustar idioma, zona horaria, estáticos y registrar la app:

```python
TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es-es'
ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'nombre_aplicacion',
]
```



## 5. Configuración de URLs y Vistas

###  URLs del proyecto

`nombre_proyecto/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nombre_app/', include('nombre_app.urls')),
]
```

###  URLs de la aplicación

Crear `nombre_app/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
]
```



## 6. Modelos (`models.py`)

```python
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    cuerpo = models.TextField()

    def __str__(self):
        return self.titulo
```



## 7. Vistas (`views.py`)

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def principal(request):
    posts = Post.objects.all()
    return render(request, 'nombre_app/principal.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'nombre_app/detalle_post.html', {'post': post})
```



## 8. Templates y static files

###  Estructura recomendada

```
nombre_app/
└── static/
    └── nombre_app/
        ├── css/
        │   └── style.css
        └── js/
            └── main.js

└── templates/
    └── nombre_app/
        ├── base.html
        ├── principal.html
        └── detalle_post.html
```



###  Template base (`base.html`)

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Mi wiki</title>
    <link rel="stylesheet" href="{% static 'nombre_app/css/style.css' %}">
</head>
<body>
    <h1>{% block titulo %}{% endblock %}</h1>

    {% block contenido %}{% endblock %}

    <script src="{% static 'nombre_app/js/main.js' %}"></script>
</body>
</html>
```



###  Template heredado (`principal.html`)

```html
{% extends 'nombre_app/base.html' %}

{% block titulo %}Entradas del blog{% endblock %}

{% block contenido %}
<ul>
    {% for post in posts %}
        <li>
            <a href="{% url 'detalle_post' pk=post.pk %}">
                {{ post.titulo }} ({{ post.autor }})
            </a>
        </li>
    {% endfor %}
</ul>
{% endblock %}
```



###  Paso de datos a templates

**Vista:**

```python
def principal(request):
    context = {
        "titulo": "Mi primer post",
        "autor": "JI",
        "cuerpo": "Este es mi primer post"
    }
    return render(request, 'nombre_app/principal.html', context)
```

**Template:**

```html
<h1>{{ titulo }}</h1>
<p>Autor: {{ autor }}</p>
<p>{{ cuerpo }}</p>
```



## 9. Migraciones

```bash
## Crear migraciones para la app
python manage.py makemigrations nombre_app

## Aplicar migraciones
python manage.py migrate nombre_app

## Migrar todo (todas las apps incluyendo admin y más)
python manage.py migrate
```



## 10. Panel de administración

###  Registrar modelo

`nombre_app/admin.py`

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

###  Crear superusuario

```bash
python manage.py createsuperuser
```



## 11. ORM y QuerySets

###  Acceder a la shell

```bash
python manage.py shell
```

####  Consultas básicas

```python
from nombre_app.models import Post

Post.objects.all()
Post.objects.get(id=1)
Post.objects.filter(autor="Patricia")
Post.objects.create(titulo="Hola", autor="A", cuerpo="Texto")
Post.objects.order_by("autor")
Post.objects.order_by("-autor")
```

####  Filtros comunes

```python
Post.objects.filter(titulo__contains="entrada")
Post.objects.filter(titulo__icontains="entrada")
Post.objects.filter(id__gt=5)
Post.objects.filter(autor__startswith="J")
Post.objects.filter(autor__endswith="z")
```



## 12. Template Tags y Filtros

###  Bucle for

```html
<ul>
{% for post in posts %}
    <li>{{ forloop.counter }}. {{ post.titulo }}</li>
{% empty %}
    <li>No hay entradas</li>
{% endfor %}
</ul>
```

####  Variables útiles

* `forloop.counter` → nº de iteración (empezando en 1)
* `forloop.first` → True si es la primera vuelta
* `forloop.last` → True si es la última

###  Condicionales

```html
{% if post.fpublicado %}
    <time>{{ post.fpublicado }}</time>
{% else %}
    <p>Aún no está publicado</p>
{% endif %}
```

###  Filtros útiles

```html
{{ post.cuerpo|linebreaksbr }}
{{ post.titulo|upper }}
{{ post.titulo|lower }}
{{ valor|default:"N/A" }}
```



## 13. Comandos útiles de Django

```bash
python manage.py runserver        ## Iniciar servidor
python manage.py makemigrations   ## Crear migraciones
python manage.py migrate          ## Aplicarlas
python manage.py createsuperuser  ## Crear admin
python manage.py shell            ## Consola interactiva Django
```