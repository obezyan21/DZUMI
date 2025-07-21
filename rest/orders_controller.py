from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from services.orders_service import OrderService
from dependencies import get_order_service

app = FastAPI()

class OrderCreateDto(BaseModel): # описывает какие данные ожидаются в теле запроса
    object_id: int
    system_type_id: int
    description: str
    comment: str
    decline_reason: str

@app.post('') # декоратор, обработчик пост запросов, в скобках потом эндпоинт юрлку вставим 
async def create_order(orders_dto: OrderCreateDto,
                       orders_service: OrderService = Depends(get_order_service)
):
    orders_service.create_new_order(orders_dto) # заявка создана