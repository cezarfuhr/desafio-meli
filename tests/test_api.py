from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Architect! The foundation is solid."}


def test_get_item_success():
    """
    Testa o endpoint GET /api/v1/items/{item_id} com ID válido.
    
    Verifica se retorna status 200 e os dados corretos do item.
    """
    item_id = "MLB123456789"
    response = client.get(f"/api/v1/items/{item_id}")
    
    assert response.status_code == 200
    
    item_data = response.json()
    assert item_data["id"] == item_id
    assert item_data["title"] == "iPhone 14 Pro Max 128GB Azul Sierra"
    assert item_data["price"] == 6499.99
    assert item_data["currency_id"] == "BRL"
    assert item_data["condition"] == "new"
    assert "description" in item_data


def test_get_item_not_found():
    """
    Testa o endpoint GET /api/v1/items/{item_id} com ID inválido.
    
    Verifica se retorna status 404 e mensagem de erro apropriada.
    """
    invalid_item_id = "INVALID123"
    response = client.get(f"/api/v1/items/{invalid_item_id}")
    
    assert response.status_code == 404
    
    error_data = response.json()
    assert "detail" in error_data
    assert invalid_item_id in error_data["detail"]


def test_get_all_test_items():
    """
    Testa se todos os itens do arquivo de dados podem ser buscados com sucesso.
    """
    test_item_ids = ["MLB123456789", "MLB987654321", "MLB555444333"]
    
    for item_id in test_item_ids:
        response = client.get(f"/api/v1/items/{item_id}")
        assert response.status_code == 200
        
        item_data = response.json()
        assert item_data["id"] == item_id
        assert "title" in item_data
        assert "price" in item_data
        assert "currency_id" in item_data
