from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_record(user_id: int, match_id: int, score: int):
    return {"user_id": user_id, "match_id": match_id, "score": score}

@router.get("/")
def get_records(gender: str, division: str, weight_class: str):
    return {"gender": gender, "division": division, "weight_class": weight_class, "results": []}

@router.get("/best_lift/")
def get_best_lift(user_id: int):
    return {"user_id": user_id, "best_lift": 150}
