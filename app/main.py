from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Nithish"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
