from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.agent import analyze_stock

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, stock: str = Form(...)):
    result, chart_data = analyze_stock(stock)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "stock": stock,
        "chart_data": chart_data
    })
