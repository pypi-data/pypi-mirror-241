import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .ws_router.connect import connect_ws

app = FastAPI()
connect_ws(app)


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", port=8005, reload=True)
