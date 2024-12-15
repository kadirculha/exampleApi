import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Create FastAPI instance
app1 = FastAPI()

# CORS configuration
origins = ["*"]
app1.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Define endpoints
@app1.get("/get_book")
async def get_book(param: str, request: Request):
    logging.info(f"Endpoint '/get_book' called with param: {param}")
    book_list = ["Nutuk", "sefiller", "Harry Potter", "kitap1", "kitap2", "kitap3"]
    if param.lower() in [item.lower() for item in book_list]:
        logging.info(f"Book '{param}' found.")
        return {"status": True, "message": "Kitap stoklarımızda bulunmaktadır"}
    logging.warning(f"Book '{param}' not found.")
    return {"status": False, "message": "Böyle bir ürünümüz yoktur lütfen farklı bir kitap deneyin"}

@app1.get("/get_forma")
async def get_forma(param: str, request: Request):
    logging.info(f"Endpoint '/get_forma' called with param: {param}")
    forma_list = ["Galatasaray", "fenerbahçe", "beşiktaş"]
    if param.lower() in [item.lower() for item in forma_list]:
        logging.info(f"Forma '{param}' found.")
        return {"status": True, "message": "Forma stoklarımızda bulunmaktadır"}
    logging.warning(f"Forma '{param}' not found.")
    return {"status": False, "message": "Böyle bir ürünümüz yoktur lütfen farklı bir forma deneyin"}

@app1.get("/get_type")
async def get_type(param: str, request: Request):
    logging.info(f"Endpoint '/get_type' called with param: {param}")
    type_list = ["parçalı", "çubuklu", "düz"]
    if param.lower() in [item.lower() for item in type_list]:
        logging.info(f"Type '{param}' found.")
        return {"status": True, "message": "Forma stoklarımızda bulunmaktadır"}
    logging.warning(f"Type '{param}' not found.")
    return {"status": False, "message": "Böyle bir ürünümüz yoktur lütfen farklı bir tür deneyin"}

@app1.get("/get_true")
async def get_true(request: Request):
    logging.info("Endpoint '/get_true' called.")
    return {"status": True, "message": "True API'si amaç api'den True cevabı gelen senaryoları simüle etmek"}

@app1.get("/get_false")
async def get_false(request: Request):
    logging.info("Endpoint '/get_false' called.")
    return {"status": False, "message": "False API'si amaç api'den False cevabı gelen senaryoları simüle etmek"}

# Run application
if __name__ == "__main__":
    uvicorn.run(app1, host="0.0.0.0", port=8010)
