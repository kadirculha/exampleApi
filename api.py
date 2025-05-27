import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import logging
from pydantic import BaseModel
from typing import Optional

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Create FastAPI instance
app = FastAPI(
    title="Mock API",
    description="Mock API for testing and development",
    version="1.0.0"
)

# CORS configuration
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Define endpoints
@app.get("/get_book")
async def get_book(param: str, request: Request):
    logging.info(f"Endpoint '/get_book' called with param: {param}")
    book_list = ["Nutuk", "sefiller", "Harry Potter", "kitap1", "kitap2", "kitap3"]
    if param.lower() in [item.lower() for item in book_list]:
        logging.info(f"Book '{param}' found.")
        return {"status": True, "message": "Kitap stoklarımızda bulunmaktadır"}
    logging.warning(f"Book '{param}' not found.")
    return {"status": False, "message": "Böyle bir ürünümüz yoktur lütfen farklı bir kitap deneyin"}

@app.get("/get_forma")
async def get_forma(param: str, request: Request):
    logging.info(f"Endpoint '/get_forma' called with param: {param}")
    forma_list = ["Galatasaray", "fenerbahçe", "beşiktaş"]
    if param.lower() in [item.lower() for item in forma_list]:
        logging.info(f"Forma '{param}' found.")
        return {"status": True, "message": "Forma stoklarımızda bulunmaktadır"}
    logging.warning(f"Forma '{param}' not found.")
    return {"status": False, "message": "Böyle bir ürünümüz yoktur lütfen farklı bir forma deneyin"}

@app.get("/get_type")
async def get_type(param: str, request: Request):
    logging.info(f"Endpoint '/get_type' called with param: {param}")
    type_list = ["parçalı", "çubuklu", "düz"]
    if param.lower() in [item.lower() for item in type_list]:
        logging.info(f"Type '{param}' found.")
        return {"status": True, "message": "Forma stoklarımızda bulunmaktadır"}
    logging.warning(f"Type '{param}' not found.")
    return {"status": False, "message": "Böyle bir ürünümüz yoktur lütfen farklı bir tür deneyin"}

@app.get("/get_true")
async def get_true(request: Request):
    logging.info("Endpoint '/get_true' called.")
    return {"status": True, "message": "True API'si amaç api'den True cevabı gelen senaryoları simüle etmek"}

@app.get("/get_false")
async def get_false(request: Request):
    logging.info("Endpoint '/get_false' called.")
    return {"status": False, "message": "False API'si amaç api'den False cevabı gelen senaryoları simüle etmek"}

# Yeni endpointler ve modeller
class OrderRequest(BaseModel):
    urun_adi: str
    adet: int
    teslimat_adresi: str

@app.post("/order_api")
async def order_api(input: OrderRequest):
    return {"status": "success",
            "message":  f"sipariş başarıyla oluşturuldu: {input.dict()}"}

class CustomerServiceRequest(BaseModel):
    sorun_tipi: str
    musteri_no: str
    aciliyet: Optional[str] = None
    iletisim_tercihi: Optional[str] = None

@app.post("/customer_service")
async def customer_service(input: CustomerServiceRequest):
    return {"status": "success",
            "message": f"sorun başarıyla tespit edildi: {input.dict()}"}

class ReturnRequest(BaseModel):
    siparis_no: str
    iade_sebebi: Optional[str] = None
    urun_durumu: str
    iade_yontemi: str

@app.post("/urun_iade_akisi")
async def urun_iade_akisi(input: ReturnRequest):
    return {
        "status": "success",
        "message": f"İade işleminiz başarı ile oluşturuldu: {input.dict()}"
    }

class ReserveRequest(BaseModel):
    hizmet_turu: str
    tarih: str
    saat: str
    kisi_sayisi: Optional[int] = None
    ozel_talepler: Optional[str] = None

@app.post("/randevu_akisi")
async def randevu_akisi(input: ReserveRequest):
    return {
        "status": "success",
        "message": f"randevu başarıyla oluşturuldu: {input.dict()}"
    }
    
class CargoRequest(BaseModel):
    siparis_no: str
    urun_adi: str
    urun_durumu: str
    adres: str
    
@app.post("/cargo_akisi")
async def cargo_akisi(input: CargoRequest):
    return {
        "status": "success",
        "message": f"cargo başarıyla oluşturuldu: {input.dict()}"
    }


# mng kargo için api senaryoları

class ShipmentRequest(BaseModel):
    sender_name: str
    sender_phone: str
    sender_email: str
    sender_address: str
    sender_city: str
    sender_district: str
    sender_postal_code: str
    receiver_name: str
    receiver_phone: str
    receiver_email: str
    receiver_address: str
    receiver_city: str
    receiver_district: str
    receiver_postal_code: str
    package_description: str
    package_weight: float
    package_length: int
    package_width: int
    package_height: int
    package_value: float
    service_type: str  # standard, express, cargo
    payment_method: str  # sender_pay, receiver_pay
    insurance: Optional[bool] = False
    sms_notification: Optional[bool] = True

@app.post("/mng_cargo/create_shipment")
async def create_shipment(shipment: ShipmentRequest):
    return {
        "status": "success",
        "message": f"Kargo oluşturuldu: {shipment.dict()}"
    }

class NearestBranchRequest(BaseModel):
    cityName: str
    districtName: str
    neighborhoodName: str

@app.post("/mng_cargo/find_nearest_branch")
async def find_nearest_branch(request: NearestBranchRequest):
    return {
        "status": "success",
        "message": f"En yakın kargo şubesi: {request.dict()}"
    }


class CargoTrackingRequest(BaseModel):
    tracking_number: str
    name: str
    phone: str

@app.post("/mng_cargo/tracking")
async def tracking(request: CargoTrackingRequest):
    return {
        "status": "success",
        "message": f"Kargo takip numarası: {request.dict()}"
    }






# Run application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8010)
