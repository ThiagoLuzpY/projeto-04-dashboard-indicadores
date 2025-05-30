from fastapi.testclient import TestClient
from backend.main import app  # ✅ Importa o app FastAPI real da pasta renomeada

client = TestClient(app)

def test_get_etl_data():
    response = client.get("/etl-data?limit=2")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    if len(data) > 0:
        item = data[0]
        assert "id" in item
        assert "fornecedor" in item
        assert "cnpj" in item
        assert "categoria" in item
        assert "data_compra" in item
        assert "valor_total" in item
