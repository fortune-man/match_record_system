from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# 통신 동작 여부를 확인하는 테스트 코드로 추정
def test_read_root():
    response = client.get("/OK")
    assert response.status_code == 200
    assert "message" in response.json()

# 선수 정보를 불로오기로 조회하고 체급별로 선택한다
def test_player_schema_sample():
    sample = {
        "name": "정재영",
        "division": "중등부",
        "gender": "남",
        "weight_class": "61kg",
        "snatch": [55, 58, 61],
        "clean_jerk": [70, 75, 80],
        "school": "정림중학교"
    }
    assert sample["weight_class"] in ["55kg","61kg","67kg","73kg","81kg","89kg"]
    assert len(sample["snatch"]) == 3
