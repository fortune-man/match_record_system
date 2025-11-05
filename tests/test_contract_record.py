from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_record_contract():
    response = client.post("/records/", params={"user_id": 1, "match_id": 2, "score": 100})
    data = response.json()
    assert response.status_code == 200
    assert "id" in data
    assert "user_id" in data
    assert "score" in data