from sqlalchemy.orm import Session 
from dao.orders_dao import OrderDAO
from config import session



def show_orders():

    order_dao = OrderDAO(session)
    orders = order_dao.get_all()

    for order in orders:
        print(f'\nID: {order.id}')
        print(f'\nObject: {order.object.name}')
        print(f'\nUser: {order.user.last_name, order.user.first_name, order.user.middle_name}')
        print(f'\nSystem Type: {order.system_type}')
        print(f'\nStatus: {order.order_status}')
        print(f'\nTotal price: {order.total_price}')
        print(f'\nAgreed?: {order.agreed}')
        print(f'\nPriority: {order.priority}')
        print(f'\nDescription: {order.description}')
        print(f'\nComment: {order.comment}')
        print(f'\nDecline_reason: {order.decline_reason}')
        print('------------------------')


def manage_orders():

    while True:
        print("\n1. Change order status")
        print("2. Create order")
        print("3. Edit order")
        print("4. Delete order")
        print("5. Show orders")
        print("0. Back to main menu")

        choice = input("Выберите: ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            show_orders()
        elif choice == "0":
            break 

    pass


def change_status():
    

        pass


def pay_order():
    pass


def add_smth():
    pass


def main_menu():
    try:
        while True:
            print("\n===Главное меню===")
            print("1. Управление заявками")
            print("2. Оплатить заявку")
            print("3. Добавить...")
            print("0. Выход\n")

            choice = input("Выберите: ")

            if choice == "1":
                manage_orders()
            elif choice == "2":
                pay_order()
            elif choice == "3":
                add_smth()
            elif choice == "0":
                break
            
    finally:
        print('\nthe session is over')

main_menu()
