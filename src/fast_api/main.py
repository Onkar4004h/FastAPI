from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app=FastAPI()
template_=Jinja2Templates(directory="templates")
@app.get("/",response_class=HTMLResponse)
def home():
    return f"<h1>HEllo world<h1>"