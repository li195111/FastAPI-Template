from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
def index(req:Request):
    return {}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=3000, reload=True, log_level='debug')

