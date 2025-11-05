# 핵심 api 입출력
def test_players_contract(client):
    response = client.post("/players", json={"id" : 1, "name" : "홍길동" , "category" : "중등부", "gender" : "남", "weight_class" : "67kg"}) 
    assert response.status_code == 200
    data = response.json()
    assert "message" in data or "id" in data
