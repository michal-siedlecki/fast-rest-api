import pytest
from fastapi.testclient import TestClient
from core.main import app


@pytest.fixture()
def client() -> TestClient:
    with TestClient(app) as c:
        yield c


@pytest.fixture
def create_date_data():
    return {"day": 15, "month": 5}


@pytest.fixture
def create_date_other_data():
    return {"day": 15, "month": 1}


@pytest.fixture
def create_wrong_date_data():
    return {"day": 55, "month": 5}
