from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
from services.items_service import ItemService
from dependencies import get_item_service
from typing import List, Optional

app = FastAPI()

class ItemDto(BaseModel):
    item_id = [int]
    order_id = [int]
    quantity = [int]
    
# я думаю как будет, у нас есть в бд таблица с товаром и типо таблица с корзинами
# добавляем товар -> у него свой айди и в таблице с корзинами у него будет айди заказа к которому он относится
# если не понял посмотри еще раз бд/модели

@app.post('')
async def add_item(item_dto: ItemDto,
                        item_service: ItemService = Depends(get_item_service)
):
    item_service.add_item(item_dto)