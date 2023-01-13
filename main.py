#FastAPI Imports
import uvicorn
from fastapi import FastAPI

#Local Imports
from config import models
from config.database import engine
from config.routes import router

app =FastAPI()
app.include_router(router)
models.Base.metadata.create_all(engine)

@app.get('/ping')
def PingView():
    '''
    Ping View
    '''
    return {"ping":"pong"}

if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)