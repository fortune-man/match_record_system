# tests/test_contract_results.py
import pytest

@pytest.mark.parametrize("gender,division,weight_class", [
    ("남자", "중등부", "67kg"),
    ("남자", "중등부", "81kg"),
])
def test_get_result_contract(client, gender, division, weight_class):
    # """고객 요구사항: 특정 성별/구분/체급의 경기 결과를 정상적으로 반환해야 함"""
    res = client.get(f"/records?gender={gender}&division={division}&weight_class={weight_class}")
    assert res.status_code == 200

    data = res.json()
    assert "players" in data
    assert all("이름" in p for p in data["players"])
    assert all("체급" in p for p in data["players"])
    assert all("결과" in p for p in data["players"])

    # 필터링 검증
    assert all(p["체급"] == weight_class for p in data["players"])
    assert all(p["구분"] == division for p in data["players"])
