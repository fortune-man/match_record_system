def test_best_lift_and_ranking(client):
    # Create records for multiple users
    client.post("/records/", params={"user_id": 1, "match_id": 1, "score": 150})
    client.post("/records/", params={"user_id": 2, "match_id": 2, "score": 200})
    client.post("/records/", params={"user_id": 3, "match_id": 3, "score": 180})
    client.post("/records/", params={"user_id": 4, "match_id": 4, "score": 220})
    client.post("/records/", params={"user_id": 5, "match_id": 5, "score": 160})
    
    # Test best lift retrieval
    response = client.get("/user_records/best_lift/", params={"user_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["best_lift"] == 200

    # Test ranking retrieval
    response = client.get("/records/ranking/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["user_id"] == 2  # Highest score
    assert data[1]["user_id"] == 1
    assert data[2]["user_id"] == 3