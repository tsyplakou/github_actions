import pytest
from app.database import get_db, AsyncSessionLocal
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def client():
    """Заменяем `get_db` на тестовую БД"""
    async def test_db():
        async with AsyncSessionLocal() as session:
            yield session
            await session.rollback()  # Откатываем изменения после теста

    app.dependency_overrides[get_db] = test_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()  # Убираем подмену после теста
