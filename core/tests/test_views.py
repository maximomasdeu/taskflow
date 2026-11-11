import pytest


@pytest.mark.django_db
def test_listar_tareas_requiere_autenticacion(cliente):
    response = cliente.get("/api/tasks/")

    assert response.status_code == 401
