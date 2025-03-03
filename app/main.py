from contextlib import asynccontextmanager

from app.database import create_tables, delete_tables
from app.routes import router
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")


app = FastAPI(lifespan=lifespan)

# Base.metadata.create_all(bind=engine)

app.include_router(router)
