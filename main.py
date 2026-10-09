from fastapi import FastApi


apo = FastApi()
@app.get("/")
def read_root():
    return {"status":"ok","message":"API funcionando"}