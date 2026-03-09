# NoticiasCiclismo – Aplicación Flask con Docker y CI/CD

## 1. Introducción

Este proyecto consiste en el desarrollo y despliegue de una aplicación web sencilla utilizando **Python y el framework Flask**, que ha sido **contenedorizada mediante Docker** y automatizada mediante un **pipeline de integración continua utilizando GitHub Actions**.

El objetivo principal de este proyecto es demostrar cómo se puede automatizar el ciclo de vida de una aplicación mediante técnicas modernas de desarrollo como:

* Contenedorización con Docker
* Integración continua (CI)
* Automatización de despliegues
* Gestión de dependencias
* Control de versiones con GitHub

La aplicación desarrollada muestra una página web básica relacionada con noticias del mundo del ciclismo.

---

# 2. Tecnologías utilizadas

Las principales tecnologías utilizadas en este proyecto son:

* **Python 3**
* **Flask** – Framework web ligero para Python
* **Docker** – Para la creación de contenedores
* **GitHub** – Control de versiones del proyecto
* **GitHub Actions** – Automatización del pipeline CI/CD
* **Docker Hub** – Registro de imágenes Docker
* **Pytest** – Framework para pruebas automatizadas

Estas herramientas permiten crear aplicaciones reproducibles, portables y fácilmente desplegables en diferentes entornos.

---

# 3. Estructura del proyecto

El repositorio se organiza de la siguiente manera:

```
NoticiasCiclismo/
│
├── .github/workflows/
│   └── docker.yml
│
├── templates/
│
├── test/
│
├── app.py
├── conftest.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

Descripción de los principales archivos:

| Archivo           | Descripción                                        |
| ----------------- | -------------------------------------------------- |
| app.py            | Aplicación principal desarrollada con Flask        |
| requirements.txt  | Lista de dependencias del proyecto                 |
| Dockerfile        | Archivo para construir la imagen Docker            |
| templates/        | Plantillas HTML de la aplicación                   |
| test/             | Pruebas automatizadas del proyecto                 |
| .github/workflows | Configuración del pipeline de integración continua |
| README.md         | Documentación del proyecto                         |

---

# 4. Aplicación Flask

La aplicación está desarrollada utilizando el framework **Flask**, que permite crear aplicaciones web de forma sencilla y rápida.

La aplicación define una ruta principal (`/`) que devuelve una página web con contenido relacionado con el ciclismo.

Ejemplo simplificado del funcionamiento:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

El servidor se ejecuta en el **puerto 5000**, que es el puerto estándar utilizado por Flask.

---

# 5. Contenerización con Docker

Para garantizar la portabilidad de la aplicación, se ha creado una imagen Docker utilizando un **Dockerfile**.

Docker permite empaquetar la aplicación junto con todas sus dependencias para que pueda ejecutarse en cualquier sistema que disponga de Docker instalado.

## Dockerfile utilizado

El archivo Dockerfile realiza las siguientes acciones:

1. Utiliza una imagen base oficial de Python.
2. Copia el archivo de dependencias.
3. Instala las dependencias necesarias.
4. Copia el código fuente de la aplicación.
5. Expone el puerto 5000.
6. Ejecuta la aplicación Flask.

Ejemplo de Dockerfile:

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

# 6. Construcción de la imagen Docker

Para construir la imagen Docker manualmente se puede utilizar el siguiente comando:

```
docker build -t noticiasciclismo .
```

Esto generará una imagen Docker con la aplicación incluida.

---

# 7. Ejecución del contenedor

Una vez construida la imagen, se puede ejecutar el contenedor con el siguiente comando:

```
docker run -p 5000:5000 noticiasciclismo
```

Después de ejecutar este comando, la aplicación estará disponible en:

```
http://localhost:5000
```

---

# 8. Integración continua con GitHub Actions

Para automatizar el proceso de construcción y despliegue de la aplicación se ha configurado un **pipeline de integración continua utilizando GitHub Actions**.

Este pipeline se ejecuta automáticamente cada vez que se realiza un push al repositorio.

El pipeline realiza las siguientes tareas:

1. Descarga el código del repositorio.
2. Construye la imagen Docker.
3. Ejecuta las pruebas automatizadas.
4. Publica la imagen en Docker Hub.

Esto permite garantizar que cada cambio en el código se verifica automáticamente.

---

# 9. Publicación en Docker Hub

La imagen generada por el pipeline se publica automáticamente en **Docker Hub**.

Esto permite descargar y ejecutar la aplicación desde cualquier máquina mediante el comando:

```
docker pull usuario/noticiasciclismo
```

Posteriormente se puede ejecutar el contenedor:

```
docker run -p 5000:5000 usuario/noticiasciclismo
```

Para permitir esta publicación automática, se han configurado los siguientes **secrets en GitHub**:

* DOCKERHUB_USERNAME
* DOCKERHUB_TOKEN

Estos secretos permiten autenticar el pipeline contra Docker Hub.

---

# 10. Pruebas automatizadas

El proyecto incluye pruebas automatizadas utilizando **pytest**.

Estas pruebas verifican que la aplicación responde correctamente cuando se accede a la ruta principal.

Ejemplo de prueba:

```python
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
```

Las pruebas se ejecutan automáticamente dentro del pipeline antes de construir la imagen Docker.

Esto ayuda a detectar errores antes de realizar el despliegue.

---

# 11. Ventajas de la contenerización y CI/CD

El uso combinado de Docker y pipelines de integración continua ofrece múltiples ventajas:

* Reproducibilidad del entorno de ejecución
* Automatización del proceso de despliegue
* Detección temprana de errores
* Mayor portabilidad entre entornos
* Simplificación de la gestión de dependencias

Estas prácticas son ampliamente utilizadas en entornos profesionales de desarrollo de software.

---

# 12. Conclusión

En este proyecto se ha desarrollado una aplicación web utilizando Flask y se ha demostrado cómo automatizar su construcción y despliegue mediante herramientas modernas de desarrollo.

La utilización de Docker permite crear aplicaciones portables y reproducibles, mientras que GitHub Actions facilita la automatización del ciclo de vida del software.

Este enfoque mejora la calidad del software y reduce el tiempo necesario para desplegar nuevas versiones de la aplicación.
