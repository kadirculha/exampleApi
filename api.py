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


@app1.get("/get_departments/")
def get_departments():
    # "basketball", "football", "volleyball"
    return {
        "result": ["Ürün Hizmetleri",
                   "Bilet Hizmetleri",
                   "İşbirliği ve Anlaşma"]
    }


@app1.get("/get_product_types/")
def get_product_types():
    # "çubuklu", "kolsuz", "hoodie"
    return {"result": ["Forma", "Ayakkabı"]}


@app1.get("/get_uniform_type/")
def get_product_by_color():
    # "yellow", "red", "green", "blue"
    return {"result": ["Çubuklu", "Düz", "Parçalı"]}


@app1.get("/get_size/")
def get_product_by_size():
    # "x", "xxl", "s"
    return {"result": ["XS", "XL", "XXL"]}


@app1.get("/get_market/")
def get_market():
    return {"result": ["www.example.com da ürününüz bulunmaktadır"]}


@app1.get("/get_food/")
def get_food():
    return {"result": ["Yemeğiniz ... restauranttadır ve yola çıkmıştır"]}


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
    uvicorn.run(app1, host="0.0.0.0", port=8000)
