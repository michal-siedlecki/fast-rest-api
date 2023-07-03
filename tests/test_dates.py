import calendar
import os


def test_read_dates(client):
    response = client.get("/dates")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_post_date(client, create_date_data):
    response = client.post("/dates", json=create_date_data)
    month_name = calendar.month_name[create_date_data.get("month")]
    assert response.status_code == 201
    assert month_name in str(response.content)


def test_popular_dates(client, create_date_data, create_date_other_data):
    client.post("/dates", json=create_date_data)
    client.post("/dates", json=create_date_data)
    client.post("/dates", json=create_date_data)
    client.post("/dates", json=create_date_other_data)
    response = client.get("/popular")
    popular_month_name = calendar.month_name[create_date_data.get("month")]
    assert response.status_code == 200
    assert type(response.json()) == list
    assert popular_month_name in str(response.json()[0])


def test_delete_date(client):
    response = client.get("/dates")
    date_id = response.json()[0].get("id")
    headers = {"X-API-HEADER": f"{os.getenv('SECRET_KEY')}"}
    delete_response = client.delete(f"/dates/{date_id}", headers=headers)
    assert delete_response.status_code == 204
    check_response = client.get("/dates")
    assert date_id not in str(check_response.content)
