import sass
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/", response_class=FileResponse)
# 정적 파일 연결 (예: 이미지, JS 등)
app.mount("/static", StaticFiles(directory="static"), name="static")
def home():
    return FileResponse("index.html")
@app.get("/style.css")
def style():
    css = sass.compile(filename="style.scss")
    return Response(content=css, media_type="text/css")
