from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class EATABLES(BaseModel):
    favourite: str
    rate: int
    confess: bool
    bae: str
    others: Optional[list]

@app.get("/groceries/{input}")

def kilo(input, w:Optional[str]=None):
    return{"fruits":"veggies","type":input,"display":w}

@app.put("/chocolates")    

async def other(fries:EATABLES):
    return{"all time favourite":fries.favourite}



