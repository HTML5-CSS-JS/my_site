from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sass_embedded import compile_file

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
def home():
    return FileResponse("index.html")

@app.get("/style.css")
def style():
    # 요청마다 style.scss를 읽고 CSS로 변환
    css = compile_file("style.scss")
    return Response(content=css, media_type="text/css")
