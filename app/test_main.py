from fastapi.testclient import TestClient
# Nuqtani olib tashladik, bu import xatosini oldini oladi
from main import app 

client = TestClient(app)

def test_read_main():
    """Asosiy sahifa (root) to'g'ri ishlayotganini tekshirish"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "success", 
        "message": "CI/CD Pipeline ishlamoqda!"
    }

def test_health_check():
    """Health check endpointini tekshirish"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_404_error():
    """Mavjud bo'lmagan sahifa so'ralganda 404 qaytarishini tekshirish"""
    response = client.get("/not-found")
    assert response.status_code == 404
