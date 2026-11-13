from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
app=FastAPI()
app.mount("/static",StaticFiles(directory="C:/fastAPI/fast_api/staic_finished"),name="static")
posts: list[dict] = [
    {
        "id": 2,
        "author": "John Doe",
        "title": "Learning Python",
        "content": "Python is a great language for beginners.",
        "date_posted": "May 10, 2025",
    },
    {
        "id": 3,
        "author": "Alice Smith",
        "title": "Getting Started with FastAPI",
        "content": "FastAPI makes building APIs simple and fast.",
        "date_posted": "June 15, 2025",
    },
    {
        "id": 4,
        "author": "David Miller",
        "title": "Why Learn Backend Development",
        "content": "Backend development helps you build powerful web applications.",
        "date_posted": "July 22, 2025",
    },
]
templates=Jinja2Templates(directory="templates")
@app.get("/",include_in_schema=False)
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts, "title":"home"})

