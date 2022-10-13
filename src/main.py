from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_predict")
async def root():
    import time
    time.sleep(5)
    return {"predict": "Your prediction :)"}
