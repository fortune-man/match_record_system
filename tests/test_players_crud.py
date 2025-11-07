def test_player_crud(client):
    # 선수 정보를 입력해서 등록하고 생성함을 의미하는 코드
    # 우리의 고객은 선수 이름  뿐이 아니라
    # 성별, 구분, 체급, 접수 번호, 성별,시도, 소속, 생년월일, 학년, 용상 (1차, 2차, 3차), 인상 (1차, 2차, 3차), 성공과 실패, 가장 큰 성공 기록, 기록 랭킹)등의 세부정보를 입력하길 원하신다.
    # 해당 erd와 연관관계 매핑 및 변경에 용이한 구조 설계에 1일 이상이 소요되었으며
    # 이 기능을 구현하기 위해 필요한 목록 정리와 테스트 대상 32개를 추리는데 3일동안 3만원 이상의 비용이 지출되었다.
    # 사용자는 자바에 익숙하고 파이썬 fastapi 문법에 대해 전혀 모르므로 필요한 코드를 추천해주며 고통관리를 즉각 개선할 필요가 있는 상황이다.
    # 따라서 아래와 같은 테스트 코드를 작성하였다.
    # 선수 등록 및 조회 테스트 코드
    # given: 선수 정보
    player_data = {
        "name": "선은혁",
        "division": "고등부",
        "gender": "남",
        "weight_class": "73kg"
    }
    # when: 선수 등록 요청
    response = client.post("/players", json=player_data)
    # then : 등록 성공 확인
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    player_id = data["id"]
    # when: 선수 조회 요청
    response = client.get(f"/players/{player_id}")
    # then: 조회 성공 및 데이터 일치 확인
    assert response.status_code == 200
    #create
    response = client.post("players", json=("선은혁"))
    assert response.status_code == 200
    data = response.json()
    assert "id" in data 
    player_id = data["id"]
    #retrieve
    response = client.get(f"/players/{player_id}")
    assert response.status_code == 200
    data = response.json()
    assert_data["name"] == "선은혁"
    #update
    response = client.put(f"/players/{player_id}", json={"weight_class": "81kg"})
    assert response.status_code == 200
    data = response.json()
    assert data["weight_class"] == "81kg"
    #delete
    response = client.delete(f"/players/{player_id}")
    assert response.status_code == 200
    #verify deletion
    response = client.get(f"/players/{player_id}")
    assert response.status_code == 404

    # 지금 이게 무슨 코드이고 어떻게 동작하고 잘 동작하는지 전혀 모르겠는데 설명 요청드릴 수 있을까요
    # 그리고 이 테스트 코드가 선수 등록, 조회, 수정, 삭제 기능을 모두 포함하고 있는지 확인 부탁드립니다.
    # 추가로 선수 목록을 불러오는 기능도 테스트 코드에 포함시켜 주실 수 있으실까요?
    # 현재 docs/features.md 파일에 명시된 선수 정보 항목들이 모두 반영되었는지도 확인 부탁드립니다.
    # Finally, could you please ensure that the test code adheres to best practices for FastAPI testing?
    # 어떻게 하면 test -> code -> production code -> test code 의 순환 구조를 잘 유지할 수 있을까요
    # 오늘 안에 로컬 앱을 완성 후 iptime 공유기로 무료 도메인 연결을 통해 외부 접속 설정을 완료하고 고객에게 시연과 배포까지 마쳐 만족도를 더블체크 3회이상 해야됩니다.
    # 터미널에 명령어 치는 것까지 도와주실 수 있으실까요
    # 예를 들면 uvicorn app.main:app --reload 이런식으로요
    # features.md 파일에 명시된 내용을 참고하여 의도대로 잘 구현되는지 확인하려면 어떤 테스트 명령어를 사용해야 되나요
    # 인공지능에게 물어봐야될지 google링을 해야될지 하나도 모릅니다
    

    #list
    response = client.get("/players")
    assert response.status_code == 200
    assert isinstance(response.json(), list)