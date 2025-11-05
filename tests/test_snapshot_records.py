def test_record_snapshot(snapshot, client):
    
    response = client.post("/records/", params={"user_id": 1, "match_id": 2, "score": 50})
    snapshot.assert_match(json.dumps(response.json(), ensure_ascii=False), "record_snapshot")