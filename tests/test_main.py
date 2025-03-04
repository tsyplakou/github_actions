def test_create_car(client):
    response = client.post("/cars/", json={"brand": "Toyota", "model": "Camry", "year": 2020})
    assert response.status_code == 200
    assert response.json()["brand"] == "Toyota"


def test_get_cars(client):
    response = client.get("/cars/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_car_not_found(client):
    response = client.get("/cars/999")
    assert response.status_code == 404
