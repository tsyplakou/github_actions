from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, database, schemas

router = APIRouter()


@router.get("/cars/", response_model=list[schemas.CarResponse])
async def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return await crud.get_cars(db, skip=skip, limit=limit)


@router.get("/cars/{car_id}", response_model=schemas.CarResponse)
async def read_car(car_id: int, db: Session = Depends(database.get_db)):
    car = await crud.get_car(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@router.post("/cars/", response_model=schemas.CarResponse)
async def create_car(car: schemas.CarCreate, db: Session = Depends(database.get_db)):
    return await crud.create_car(db, car)


@router.delete("/cars/{car_id}", status_code=204)
async def delete_car(car_id: int, db: Session = Depends(database.get_db)):
    if not crud.delete_car(db, car_id):
        raise HTTPException(status_code=404, detail="Car not found")
    return {"message": "Car deleted"}
