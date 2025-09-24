# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_send_email():
    response = client.post("/send-email/?recipient=test@example.com")
    assert response.status_code == 200
    assert response.json()["status"] == "Email task queued"

def test_job_status():
    # Step 1: Trigger email task
    response = client.post("/send-email/?recipient=test@example.com")
    assert response.status_code == 200
    job_id = response.json()["job_id"]

    # Step 2: Check job status
    status_response = client.get(f"/status/{job_id}")
    assert status_response.status_code == 200
    assert status_response.json()["status"] in ["queued", "started", "finished"]