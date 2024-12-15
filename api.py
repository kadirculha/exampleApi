import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import logging
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

logging.basicConfig(level=logging.INFO)

@app1.middleware("http")
async def log_requests(request: Request, call_next):
    idem = request.headers.get("x-request-id", "N/A")
    logger = logging.getLogger("uvicorn.access")
    logger.info(f"rid={idem} start request path={request.url.path}")
    response = await call_next(request)
    logger.info(f"rid={idem} completed_in={response.headers.get('x-process-time')} status_code={response.status_code}")
    return response

@app1.get("/get_book")
def get_book(param: str):
    book_list = ["Nutuk", "sefiller", "Harry Potter", "kitap1", "kitap2", "kitap3"]
    logging.info(f"Checking availability for book: {param}")

    if param.lower() in [item.lower() for item in book_list]:
        logging.info("Book available in stock.")
        return {"status": True,
                "message": "Kitap stoklarımızda bulunmaktadır"}
    logging.warning("Book not available.")
    return {"status": False,
            "message": "Böyle bir ürünümüz yoktur lütfen farklı bir kitap deneyin"}

@app1.get("/get_forma")
def get_forma(param: str):
    book_list = ["Galatasaray", "fenerbahçe", "beşiktaş"]
    logging.info(f"Checking availability for forma: {param}")

    if param in [item.lower() for item in book_list]:
        logging.info("Forma available in stock.")
        return {"status": True,
                "message": "Forma stoklarımızda bulunmaktadır"}
    logging.warning("Forma not available.")
    return {"status": False,
            "message": "Böyle bir ürünümüz yoktur lütfen farklı bir forma deneyin"}

@app1.get("/get_type")
def get_type(param: str):
    book_list = ["parçalı", "çubuklu", "düz"]
    logging.info(f"Checking availability for type: {param}")

    if param in [item.lower() for item in book_list]:
        logging.info("Type available in stock.")
        return {"status": True,
                "message": "Forma stoklarımızda bulunmaktadır"}
    logging.warning("Type not available.")
    return {"status": False,
            "message": "Böyle bir ürünümüz yoktur lütfen farklı bir tür deneyin"}

@app1.get("/get_true")
def get_true():
    logging.info("get_true endpoint was called")
    return {"status": True,
            "message": "True API'si amaç api'den True cevabı gelen senaryoları simüle etmek"}

@app1.get("/get_false")
def get_false():
    logging.info("get_false endpoint was called")
    return {"status": False,
            "message": "False API'si amaç api'den False cevabı gelen senaryoları simüle etmek"}

@app1.get("/handle_media")
def handle_media(param: str):
    allowed_types = ["AUDIO", "IMAGE", "VIDEO", "DOCUMENT", "FILE", "TEXT"]
    logging.info(f"Handling media type: {param}")

    if param.upper() in allowed_types:
        logging.info("Media type is allowed.")
        return {"status": True,
                "message": f"{param} tipi talepler kabul edilmektedir."}
    logging.warning("Media type not allowed.")
    raise HTTPException(status_code=400, detail="Bu tip talepler kabul edilmemektedir.")

if __name__ == "__main__":
    uvicorn.run(app1, host="0.0.0.0", port=8010)
