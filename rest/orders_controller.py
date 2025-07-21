from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
from services.orders_service import OrderService
from dependencies import get_order_service
from typing import List

app = FastAPI()

class OrderCreateDto(BaseModel): # описывает какие данные ожидаются в теле запроса
    object_id: int
    system_type_id: int
    description: str
    comment: str
    decline_reason: str


class OrderResponceDto(BaseModel):  # дто для ответа
    id: int
    object_id: int
    user_id: int  # мб поменять на ФИО
    system_type: int
    order_status: str
    total_price: float
    agreed: str
    priority: int
    description: str
    comment: str
    decline_reason: str


@app.post('') # декоратор, обработчик пост запросов, в скобках потом эндпоинт юрлку вставим 
async def create_order(orders_dto: OrderCreateDto,
                       orders_service: OrderService = Depends(get_order_service)
):
    orders_service.create_new_order(orders_dto) # заявка создана

# Эндпоинт с пагинацией
@app.get("/orders", response_model=List[OrderResponceDto])
async def get_orders(
    skip: int = Query(0, ge=0, description="Сколько записей пропустить"),
    limit: int = Query(10, le=100, description="Лимит записей на страницу"),
    order_service: OrderService = Depends(get_order_service)
):
    return await order_service.get_all_orders(skip=skip, limit=limit)