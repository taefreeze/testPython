#Author: Tae Chanwit
#Date: December 23,2020.

from fastapi import FastAPI
from typing import Optional
import uvicorn
import numpy as np
from bson import ObjectId
import re
import math
import requests
from bs4 import BeautifulSoup
from fastapi.responses import PlainTextResponse
from collections import Counter


app = FastAPI()

def result(res):
    return {"result":res}
@app.get("/")
async def main():
    return 'Hello World'

if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True) 