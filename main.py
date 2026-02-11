import sass
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
@app.get("/style.css")
def home():
    return print(t"log")
def get_css():
    css = sass.compile(filename="/style.scss")
    return Response(content=css, media_type="text/css")
