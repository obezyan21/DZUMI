from sqlalchemy.orm import Session
from models.order import Order
from .base_dao import BaseDAO


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

    def save(self, request):
        pass

    def update_status(self, request, new_status):
        '''Меняем статус через модель'''
        request.change_status(new_status)  # change_status - вызываем у модели Order
        self.save(request)
    