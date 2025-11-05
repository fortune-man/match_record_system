# main.py (핵심 API들 복원)

from fastapi import FastAPI, Query
from pydantic import BaseModel
import json

app = FastAPI()

# --- Models ---
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

# --- Mock Storage ---
players_db = []
records_db = []

# --- Endpoints ---

@app.post("/players/")
def create_player(player: Player):
    players_db.append(player.dict())
    return player

@app.post("/records/")
def create_record(user_id: int, match_id: int, score: int):
    new_id = len(records_db) + 1
    record = {"id": new_id, "user_id": user_id, "match_id": match_id, "score": score}
    records_db.append(record)
    return record

@app.get("/records")
def get_results(gender: str, division: str, weight_class: str):
    # 고객 스펙 맞춰서 players 필드 추가
    return {
        "gender": gender,
        "division": division,
        "weight_class": weight_class,
        "players": players_db,  # 빈 리스트여도 구조 필요
        "results": [],
    }

@app.get("/records/best_lift/")
def best_lift(user_id: int):
    user_records = [r for r in records_db if r["user_id"] == user_id]
    if not user_records:
        return {"best_lift": 0}
    best = max(records_db, key=lambda r: r["score"])
    return {"best_lift": best["score"]}

# --- Snapshot 보조 함수 ---
def snapshot_match(snapshot, response_json):
    snapshot.assert_match(json.dumps(response_json, ensure_ascii=False), "record_snapshot")
