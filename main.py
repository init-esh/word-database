
from fastapi import FastAPI , Request, Form
from fastapi.templating import Jinja2Templates

app=FastAPI()

template = Jinja2Templates(directory='templates')
words=[]

@app.get("/")
def root(request: Request):
    return template.TemplateResponse('index.html',{'request': request,'words':words})

@app.post("/add")
def add_word(word: str = Form(...)):
    words.append(word)
    return {"message":"Word added"}
