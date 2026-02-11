import sass
from fastapi import FastAPI, Response
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/style.css")
    css = sass.compile(filename="/style.scss")
    return Response(content=css, media_type="text/css")
# static 디렉토리 연결 (예: style.css, script.js 등)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
def home():
    return "index.html"
