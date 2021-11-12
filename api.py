from fastapi import FastAPI, Depends
from typing import List
import schemas
import nekofiDB as nkdb

nkdb.metadata.create_all(nkdb.engine)
app = FastAPI()


@app.on_event("startup")
async def connect():
    await nkdb.nekoDB.connect()

@app.on_event("shutdown")
async def shutdown():
    await nkdb.nekoDB.disconnect()


@app.get("/")
def home():
    return{"greeting": "Irashai~ Nekofi shop desu!"}


@app.post(f"/host-update/", response_model=schemas.Kofi)
async def newKofi(r: schemas.updateKofi = Depends()):
    query = nkdb.kofiTable.insert().values(
        title = r.title,
        description = r.description,
        price = r.price,
        isAvailable = r.isAvailable
    )
    record_id = await nkdb.nekoDB.execute(query)
    query = nkdb.kofiTable.select().where(nkdb.kofiTable.c.id == record_id)
    row = await nkdb.nekoDB.fetch_one(query)
    return {**row}


@app.put("/host-update/{title}", response_model=schemas.Kofi)
async def updateKofi(title, r: schemas.updateKofi = Depends()):
    query = nkdb.kofiTable.update().where(nkdb.kofiTable.c.title == title).values(
        title = r.title,
        description = r.description,
        price = r.price,
        isAvailable = r.isAvailable
    )
    record_id = await nkdb.nekoDB.execute(query)
    query = nkdb.kofiTable.select().where(nkdb.kofiTable.c.id == record_id)
    row = await nkdb.nekoDB.fetch_one(query)
    return {**row}


@app.get("/KofiTable/{title}", response_model=schemas.Kofi)
async def getKofi(title: str):
    query = nkdb.kofiTable.select().where(nkdb.kofiTable.c.title == title)
    kofi = await nkdb.nekoDB.fetch_one(query)
    return {**kofi}


@app.get("/KofiTable/", response_model=List[schemas.Kofi])
async def getAllKofi():
    query = nkdb.kofiTable.select()
    kofiList = await nkdb.nekoDB.fetch_all(query)
    return kofiList


@app.delete("/host-update/{title}", response_model=schemas.Kofi)
async def delete(title: str):
    query = nkdb.kofiTable.delete().where(nkdb.kofiTable.c.title == title)
    r = await nkdb.nekoDB.execute(query)
    pass