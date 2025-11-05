def test_player_crud(client):
    #create
    response = client.post("players", json=("선은혁"))
    assert response.status_code == 200

    #list
    response = client.get("/players")
    assert response.status_code == 200
    assert isinstance(response.json(), list)