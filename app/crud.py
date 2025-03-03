from app import models, schemas
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_cars(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Car).offset(skip).limit(limit))
    return result.scalars().all()


async def get_car(db: AsyncSession, car_id: int):
    result = await db.execute(select(models.Car).filter(models.Car.id == car_id))
    return result.scalar_one_or_none()


async def create_car(db: AsyncSession, car: schemas.CarCreate):
    db_car = models.Car(**car.model_dump())
    db.add(db_car)
    await db.commit()
    await db.refresh(db_car)
    return db_car


async def delete_car(db: AsyncSession, car_id: int):
    result = await db.execute(select(models.Car).filter(models.Car.id == car_id))
    db_car = result.scalars().first()

    if db_car:
        await db.delete(db_car)
        await db.commit()
        return True
    return False
