# app/main.py
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

# ----------------------------
# 🧩 데이터 모델
# ----------------------------
# Player와 Record는 고객 요구사항과 테스트 케이스 양쪽을 만족해야 합니다.
class Player(BaseModel):
    id: int
    name: str
    category: str
    gender: str
    weight_class: str

class Record(BaseModel):
    id: int
    user_id: int
    match_id: int
    score: int

# ----------------------------
# 💾 임시 저장소 (테스트 환경용)
# ----------------------------
players_db = []
records_db = []

# ----------------------------
# 🧪 루트 엔드포인트 (테스트 연결 확인용)
# ----------------------------
@app.get("/")
def read_root():
    return {"status": "ok"}

# ----------------------------
# 👤 선수 생성 API
# ----------------------------
@app.post("/players/")
def create_player(player: Player):
    # model_dump는 Pydantic v2 표준 직렬화 방식
    players_db.append(player.model_dump())
    return player

# ----------------------------
# 🏋️‍♂️ 경기 기록 생성 API
# ----------------------------
@app.post("/records/")
def create_record(user_id: int, match_id: int, score: int):
    new_id = len(records_db) + 1
    record = {"id": new_id, "user_id": user_id, "match_id": match_id, "score": score}
    records_db.append(record)
    return record

# ----------------------------
# 🧾 특정 조건의 경기 결과 조회 API
# ----------------------------
@app.get("/records")
def get_results(gender: str, division: str, weight_class: str):
    # 고객 요구사항: '이름' 필드 포함된 결과를 반환해야 함
    filtered_players = [
        {"이름": p["name"], "점수": 0, "순위": None}
        for p in players_db
        if p["gender"] == gender and p["weight_class"] == weight_class
    ]
    return {
        "gender": gender,
        "division": division,
        "weight_class": weight_class,
        "players": filtered_players,
        "results": [],
    }

# ----------------------------
# 🥇 개인 최고 기록 조회 API
# ----------------------------
@app.get("/records/best_lift/")
def best_lift(user_id: int):
    user_records = [r for r in records_db if r["user_id"] == user_id]
    if not user_records:
        return {"best_lift": 0}
    best = max(user_records, key=lambda r: r["score"])
    return {"best_lift": best["score"]}


@app.get("/OK")
def read_ok():
    return {"status": "ok"}

# ----------------------------
# 📸 Snapshot 테스트 대응
# ----------------------------
def snapshot_match(snapshot, response_json):
    import json
    # snapshot plugin은 문자열만 비교 가능하므로 변환 필요
    snapshot.assert_match(json.dumps(response_json, ensure_ascii=False), "record_snapshot")
