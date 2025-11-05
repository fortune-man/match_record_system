from fastapi import APIRouter

router = APIRouter()

# 라우터 파일 샘플
@router.post("/")
def create_player(player: dict):
    return {"message": "player created", "player": player}
