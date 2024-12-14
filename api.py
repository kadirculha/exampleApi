import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import re

app1 = FastAPI()

origins = ["*"]

app1.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)



@app1.get("/get_book")
def get_book(param):
    book_list = ["Nutuk", "sefiller", "Harry Potter", "kitap1", "kitap2", "kitap3"]

    if param.lower() in [item.lower() for item in book_list]:
        return {"status": True,
                "message": "Kitap stoklarımızda bulunmaktadır"}
    return {"status": False,
            "message": "Böyle bir ürünümüz yoktur lütfen farklı bir kitap deneyin"}


@app1.get("/get_forma")
def get_forma(param):
    book_list = ["Galatasaray", "fenerbahçe", "beşiktaş"]

    if param in [item.lower() for item in book_list]:
        return {"status": True,
                "message": "Forma stoklarımızda bulunmaktadır"}
    return {"status": False,
            "message": "Böyle bir ürünümüz yoktur lütfen farklı bir forma deneyin"}


@app1.get("/get_type")
def get_type(param):
    book_list = ["parçalı", "çubuklu", "düz"]

    if param in [item.lower() for item in book_list]:
        return {"status": True,
                "message": "Forma stoklarımızda bulunmaktadır"}
    return {"status": False,
            "message": "Böyle bir ürünümüz yoktur lütfen farklı bir tür deneyin"}


@app1.get("/get_true")
def get_true():

    return {"status": True,
            "message": "True API'si amaç api'den True cevabı gelen senaryoları simüle etmek"}


@app1.get("/get_false")
def get_false():
    return {"status": False,
            "message": "False API'si amaç api'den False cevabı gelen senaryoları simüle etmek"}


if __name__ == "__main__":
    uvicorn.run(app1, host="0.0.0.0", port=8008)
