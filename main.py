import sass
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
@app.get("/style.css")
    css = sass.compile(filename="/style.scss")
    return Response(content=css, media_type="text/css")
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html").read()
