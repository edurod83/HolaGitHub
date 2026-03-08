# Web de Ciclismo Número 1

Aplicación web simple desarrollada en **Python** con **Flask** que muestra un mensaje de bienvenida al acceder a la raíz del sitio.

## Estructura del proyecto

```
HolaGitHub/
├── .github/
│   └── workflows/
│       └── github-pipeline.yml  # Pipeline CI/CD (GitHub Actions)
├── test/
│   └── test_app.py              # Tests con pytest
├── app.py                       # Aplicación Flask
├── conftest.py                  # Configuración de pytest
├── Dockerfile                   # Imagen Docker
├── requirements.txt             # Dependencias Python
├── .gitignore
└── README.md
```

## Requisitos

- Python 3.12+
- pip

## Instalación y ejecución en local

```bash
# 1. Crear y activar el entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1      # Windows
source venv/bin/activate         # Linux/Mac

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Arrancar la aplicación
python app.py
```

La app estará disponible en: [http://localhost:5000](http://localhost:5000)

Respuesta esperada:
```
Hola, bienvenido a la web de ciclismo número 1 en el mundo!
```

## Ejecutar los tests

```bash
pytest test/ -v
```

Los tests cubren:

| Test | Descripción |
|---|---|
| `test_index_status_code` | La ruta `/` devuelve HTTP 200 |
| `test_index_message` | La respuesta contiene el mensaje de bienvenida |
| `test_index_content_type` | El `Content-Type` es `text/html` |
| `test_ruta_no_existente` | Una ruta desconocida devuelve HTTP 404 |

## Docker

### Construir la imagen

```bash
docker build -t hola-github .
```

### Ejecutar el contenedor

```bash
docker run -p 5000:5000 hola-github
```

### Publicar en Docker Hub

```bash
docker login
docker tag hola-github <TU_USUARIO>/hola-github:latest
docker push <TU_USUARIO>/hola-github:latest
```

## CI/CD con GitHub Actions

El archivo `.github/workflows/github-pipeline.yml` define un pipeline automático con dos jobs:

1. **Test** — se ejecuta en cada push o pull request a `main`:
   - Instala las dependencias
   - Ejecuta `pytest test/ -v`

2. **Docker** — solo se ejecuta si los tests pasan:
   - Construye la imagen Docker
   - La publica en Docker Hub

### Secrets necesarios en GitHub

Ve a `Settings → Secrets and variables → Actions` y añade:

| Secret | Descripción |
|---|---|
| `DOCKERHUB_USERNAME` | Tu usuario de Docker Hub |
| `DOCKERHUB_TOKEN` | Token de acceso de Docker Hub |

Los tokens se generan en Docker Hub: `Account Settings → Personal access tokens`.
