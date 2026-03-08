import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_status_code(client):
    """La ruta / debe devolver HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_index_message(client):
    """La ruta / debe contener el mensaje de bienvenida."""
    response = client.get("/")
    assert "Hola, bienvenido a la web de ciclismo número 1" in response.data.decode("utf-8")


def test_index_content_type(client):
    """La respuesta debe ser de tipo texto."""
    response = client.get("/")
    assert "text/html" in response.content_type


def test_ruta_no_existente(client):
    """Una ruta desconocida debe devolver HTTP 404."""
    response = client.get("/no-existe")
    assert response.status_code == 404
