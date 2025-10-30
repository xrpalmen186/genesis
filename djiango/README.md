# Apuntes de Django

## 1. Introducción a Django

### ¿Qué es Django?
- **Framework de desarrollo web** en Python
- Simplifica el desarrollo de aplicaciones web **robustas y escalables**
- Sitios famosos que usan Django: Instagram, Pinterest

### Características principales
- Basado en el principio **DRY** (Don't Repeat Yourself)
- Muchas funcionalidades **integradas**
- **Seguridad**: protección contra inyección SQL, XSS, CSRF
- Arquitectura **MVT** (Modelo-Vista-Template)

### Ventajas de Django
- Rápido y fácil de configurar
- Excelente para proyectos grandes y pequeños
- Enfoque en reutilización de código y modularidad
- Amplia comunidad y documentación

---

## 2. Configuración del Entorno

### Creación del entorno virtual
```bash
# Crear carpeta del proyecto
mkdir primerproyecto
cd primerproyecto

# Crear y activar entorno virtual
python3 -m venv env
source env/bin/activate

# Para salir del entorno virtual
deactivate
```

### Instalación de Django
```bash
# Crear requirements.txt con contenido: Django==5.1.3
pip install -r requirements.txt

# Verificar instalación
django-admin --version
```

---

## 3. Estructura de Proyecto Django

### Creación de proyecto y aplicación
```bash
# Crear proyecto (¡importante el punto!)
django-admin startproject nombre_proyecto .

# Crear aplicación
python manage.py startapp nombre_aplicacion
```

### Archivos principales
- **manage.py**: Herramienta para comandos
- **settings.py**: Configuraciones del proyecto
- **urls.py**: Configuración de rutas
- **views.py**: Lógica de las vistas
- **models.py**: Definición de modelos
- **admin.py**: Configuración del panel de administración

### Configuración inicial en settings.py
```python
TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es-es'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
ALLOWED_HOSTS = ['127.0.0.1']

# Registrar la aplicación creada
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Tu aplicación
]
```

---

## 4. Arquitectura MVT

### Modelo-Vista-Template (MVT)
- **Modelo**: Define estructura de base de datos y relaciones
- **Vista**: Contiene la lógica de la aplicación
- **Template**: Sistema de plantillas para la interfaz de usuario

### Componentes principales de Django
- **Django ORM**: Mapeo objeto-relacional
- **Sistema de URL**: Definición de rutas con expresiones regulares
- **Formularios**: Creación y validación
- **Admin site**: Panel de administración automático

---

## 5. Configuración de URLs y Vistas

### URLs del proyecto
```python
# proyecto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

### URLs de la aplicación
```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
]
```

### Vistas básicas
```python
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def principal(request):
    context = Post.objects.all()
    return render(request, 'blog/principal.html', {'posts': context})

def detalle_post(request, pk):
    context = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': context})
```

---

## 6. Templates

### Estructura de templates
```
blog/
└── templates/
    └── blog/
        ├── base.html
        ├── principal.html
        └── detalle_post.html
```

### Template base
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi blog</title>
</head>
<body>
    <h1>{% block titulo %}{% endblock %}</h1>
    {% block contenido %}
    {% endblock %}
</body>
</html>
```

### Template que extiende base
```html
{% extends 'blog/base.html' %}

{% block titulo %}Entradas del blog{% endblock %}

{% block contenido %}
<ul>
{% for post in posts %}
    <li><a href="{% url 'detalle_post' pk=post.pk %}">{{ post.titulo }} ({{ post.autor }})</a></li>
{% endfor %}
</ul>
{% endblock %}
```

### Paso de parámetros a templates
```python
# En views.py
def principal(request):
    context = {
        "titulo": "Mi primer post",
        "autor": "JI",
        "cuerpo": "Este es mi primer post"
    }
    return render(request, 'blog/principal.html', context)
```

```html
<!-- En template -->
<h1>{{ titulo }}</h1>
<p>Autor: {{ autor }}</p>
<p>{{ cuerpo }}</p>
```

---

## 7. Modelos

### Definición de modelos
```python
# blog/models.py
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    cuerpo = models.TextField()
    
    def __str__(self):
        return self.titulo
```

### Migraciones
```bash
# Preparar migraciones
python3 manage.py makemigrations blog

# Aplicar migraciones
python3 manage.py migrate blog

# Migrar todas las aplicaciones
python3 manage.py migrate
```

### Panel de administración
```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

```bash
# Crear superusuario
python3 manage.py createsuperuser
```

---

## 8. ORM y QuerySets

### Consultas básicas
```python
# Acceder a la shell de Django
python manage.py shell

>>> from blog.models import Post

# Obtener todos los objetos
>>> Post.objects.all()

# Obtener un objeto específico
>>> Post.objects.get(id=1)

# Filtrar objetos
>>> Post.objects.filter(autor='Patricia')

# Crear objetos
>>> Post.objects.create(titulo="Mi primer post", autor='JI', cuerpo='Texto de prueba')

# Ordenar objetos
>>> Post.objects.order_by('autor')
>>> Post.objects.order_by('-autor')  # Orden descendente
```

### Operadores de búsqueda
```python
# Contains (contiene)
Post.objects.filter(titulo__contains='entrada')

# Icontains (case insensitive)
Post.objects.filter(titulo__icontains='entrada')

# Greater than/Less than
Post.objects.filter(id__gt=5)  # id > 5
Post.objects.filter(id__lt=10) # id < 10

# Startswith/Endswith
Post.objects.filter(autor__startswith='J')
Post.objects.filter(autor__endswith='z')
```

---

## 9. Archivos Estáticos

### Configuración
```python
# settings.py
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
```

### Estructura de estáticos
```
blog/
└── static/
    └── css/
        └── blog.css
```

### Uso en templates
```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <title>Mi blog</title>
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
</head>
<body>
    <!-- contenido -->
</body>
</html>
```

---

## 10. Template Tags y Filtros

### Bucle for
```html
<ul>
{% for post in posts %}
    <li>
        <a href="{% url 'detalle_post' pk=post.pk %}">
            {{ forloop.counter }}. {{ post.titulo }}
        </a>
    </li>
{% empty %}
    <li>No tiene entradas</li>
{% endfor %}
</ul>
```

### Variables del bucle for
- `forloop.counter`: Iteración actual (1-indexed)
- `forloop.counter0`: Iteración actual (0-indexed)
- `forloop.revcounter`: Iteraciones hasta el final (1-indexed)
- `forloop.first`: True si es la primera iteración
- `forloop.last`: True si es la última iteración

### Condicionales
```html
{% if post.fpublicado %}
    <time class="date">{{ post.fpublicado }}</time>
{% else %}
    <p>Aún no está publicado</p>
{% endif %}
```

### Filtros comunes
```html
{{ post.cuerpo|linebreaksbr }}  <!-- Convierte saltos de línea en <br> -->
{{ post.titulo|upper }}         <!-- Convertir a mayúsculas -->
{{ post.titulo|lower }}         <!-- Convertir a minúsculas -->
{{ value|default:"N/A" }}       <!-- Valor por defecto -->
```

---

## 11. Comandos Útiles

### Desarrollo
```bash
# Ejecutar servidor de desarrollo
python3 manage.py runserver

# Crear migraciones
python3 manage.py makemigrations

# Aplicar migraciones
python3 manage.py migrate

# Crear superusuario
python3 manage.py createsuperuser

# Acceder a la shell de Django
python3 manage.py shell
```

### Control de versiones (Git)
- Inicializar repositorio Git
- Crear `.gitignore` para excluir `env/`, `*.pyc`, `__pycache__/`, `db.sqlite3`
- Hacer commits regulares del código

---

## 12. Recursos Adicionales

### Documentación oficial
- **Model field types**: https://docs.djangoproject.com/es/5.1/ref/models/fields/
- **Queries**: https://docs.djangoproject.com/en/5.1/topics/db/queries/
- **Template tags**: https://docs.djangoproject.com/es/5.1/ref/templates/builtins/
- **Template filters**: https://docs.djangoproject.com/es/5.1/ref/templates/builtins/#built-in-filter-reference

### Retos sugeridos
- Crear página `autores.html` que muestre distintos autores
- Modificar proyecto para incluir modelo Autor con Foreign Key
- Experimentar con diferentes tipos de campos en modelos
- Probar operadores avanzados de QuerySets
- Implementar `aggregate()` y `annotate()` en consultas