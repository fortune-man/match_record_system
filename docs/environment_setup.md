## 개요
1. 프로젝트명 : match_record_system
2. 목표 : 실사용 가능한 경기 기록 시스템 구현
3. 필요 조건
 3.1 이른 최적화 지양
 3.2 병목 기준 실용적 선택
 3.3 테스트 가능한 작은 단위부터 점진적 확장
 3.4 실행 가능 상태 상시 유지

## 절차
1. 가상환경 생성 및 활성화
```
python3 -m venv venv
source venv/bin/activate
```
- (venv) 표시로 활성화 홧인

2. 필수 패키지 설치
```
from fast api import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "fast api 연결 확인"}
```

서버 실행
```
uvicorn app.main:app --reload
```

- 브라우저에서 `http://127.0.0.1:8000` 접속 시 JSON 출력 확인
- 실패 시 포트 충돌 또는 잘못된 실행 위치 점검
    - 실행 위치 : 프로젝트 루트
    - app/ 내부에서 실행하는 실수 1회

3. 품질 점검 루틴
  3.1 코드 스타일 점검
  ```
  pip install flake8
  flake8 app/
  ```
  - zsh: command not found: flake8 -> 미설치 상태. 재시도 필요
  3.2 의존성 점검
  ```pip check```
  - 결과가  `No broken requirements found.`면 통과
  3.3 실행 점검
  `curl http://127.0.0.1:8000`
  - 서버 응답이 JSON 형식이면 ok
  - 실패 시 로그 파일 확인 필요 (uvicorn 실행 창 에러내용)

4. git 관리 루틴
  4.1 초기화 및 상태 확인
  ```
  git init
  git add .
  git commit -m "프로젝트 환경 설정"
  ```
  4.2 원격 연결
  ```
  git remote add origin <github_repo_url>
  git push -u origin main
  ```
  4.3 커밋 기준
  - 환경 변화 시점마다 커밋 (ex. 패키지 추가, 디렉토리 구조 변경)
  - 커밋 메시지 예시
    - chore : setup FastAPI environment
    - fix : uvicorn run path issue

5. 안정화 완료 체크리스트
  5.1 가상환경 정상 작동 - (venv) 확인
  5.2 fast api 기본 실행 성공 - 127.0.0.1:8000 응답
  5.3 requirements.txt 생성 - pip freeze 결과 포함
  5.4 flake8 점검 통과 - 코드 스타일 통과
  5.5 git 초기화 완료 - push 정상 완료

6. 환경 엔트로피 방지 루틴
- 매일 개발 전, 아래 명령으로 상태 점검
```
git status
pip check
flake8 app/
```
fastapi 서버가 바로 실행되지 않으면
1. venv 활성화 확인
2. 실행 디렉토리 확인
3. uvicorn 로그 확인
- 문제 발생 시 로그를 그대로 복사해 이슈 트래킹 노트 (docs/troubleshooting.md)에 추가