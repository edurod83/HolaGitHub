# VeloNoticias – La web de ciclismo número 1 en el mundo

Aplicación web desarrollada en **Python** con **Flask** que simula un portal de noticias de ciclismo. Muestra una portada con noticias ficticias, ranking UCI, próximas carreras y breves, usando plantillas Jinja2 y estilos CSS integrados.

## Capturas


La portada incluye:

- **Header** con logo, eslogan y menú de navegación
- **Ticker de última hora** animado
- **Noticia destacada** con extracto completo
- **Cuadrícula de noticias** con tarjetas interactivas
- **Sidebar** con ranking UCI World Tour, próximas carreras y breves

## Estructura del proyecto

```
HolaGitHub/
├── .github/
│   └── workflows/
│       └── github-pipeline.yml  # Pipeline CI/CD (GitHub Actions)
├── templates/
│   └── index.html               # Plantilla Jinja2 de la portada
├── test/
│   └── test_app.py              # Tests con pytest
├── app.py                       # Aplicación Flask + datos ficticios
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

La portada renderiza la plantilla `templates/index.html` con los datos definidos en `app.py`:

| Variable | Contenido |
|---|---|
| `noticias` | Lista de 6 noticias ficticias con título, extracto, categoría, autor y fecha |
| `ranking` | Top 7 del ranking UCI World Tour |
| `proximas_carreras` | 5 próximas carreras del calendario |
| `breves` | 5 noticias cortas de última hora |

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
