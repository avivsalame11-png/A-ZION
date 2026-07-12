from fastapi.testclient import TestClient
from apps.api.main import app

client = TestClient(app)


def test_create_asset():
    response = client.post("/assets", json={
        "asset_id": "AST-GR003",
        "gold_reference_id": "GR003",
        "name": "Visa Inc.",
        "ticker": "V",
        "exchange": "NYSE",
        "asset_type": "equity",
        "sector": "Financials",
        "industry": "Payment Networks",
        "country": "USA",
        "currency": "USD"
    })
    assert response.status_code == 200
    assert response.json()["lifecycle_status"] == "candidate"


def test_invalid_transition_candidate_to_certified():
    client.post("/assets", json={
        "asset_id": "AST-TEST",
        "name": "Test Asset",
        "asset_type": "equity"
    })
    response = client.post("/assets/AST-TEST/transition", json={
        "target_status": "certified",
        "reason": "invalid"
    })
    assert response.status_code == 400
