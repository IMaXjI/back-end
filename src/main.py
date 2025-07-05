from src import model
from src.db import Database
from src.route import router
from fastapi import FastAPI


app = FastAPI()
app.include_router(router)
engine = Database.get_engine()
session = Database.get_session()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(model.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()
