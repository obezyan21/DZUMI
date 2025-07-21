from sqlalchemy.orm import Session
from models.order import Order
from .base_dao import BaseDAO
from sqlalchemy import select
from typing import List


class OrderDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, Order)

    def get_by_priority(self, priority):
        return self.session.query(Order).filter(Order.priority == priority).all() # self.session.query(Order)
                                                                                  # self.session - это сессия SQLAlchemy, подключение к БД
                                                                                  # .query(Order) - создаёт новый запрос (Query object) для модели Order
                                                                                  # .filter(Order.priority == priority)
                                                                                  # Order.priority - ссылается на столбец priority в таблице orders
                                                                                  # == priority - сравнение с переданным значением
                                                                                  # .all() Выполняет собранный запрос в БД, Возвращает все строки результата как список объектов Order
                                                                                  # Если нет результатов - вернёт пустой список
                                                                                  # Это типо базовая конструкция стоит на заметку взять

    def get_by_date(self, date):
        pass

    # def get_all(self, skip: int, limit: int):  # пагинация
    #     query = select(Order).offset(skip).limit(limit)
    #     result = self.ession.execute(query)
    #     return result.scalars().all()

    def save(self, request):
        pass

    def update_status(self, request, new_status):
        '''Меняем статус через модель'''
        request.change_status(new_status)  # change_status - вызываем у модели Order
        self.save(request)

    def get_by_user(self, user: int) -> List[Order]:
        '''Получение заявок по пользователю'''
        query = select(Order).where(Order.user_id == user)
        result = self.session.execute(query)

        return result.scalars().all()
    
    
