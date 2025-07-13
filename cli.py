from dao.orders_dao import OrderDAO




def show_orders():

    order_dao = OrderDAO(session)



    pass


def manage_order():

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
            print("1. Показать заказы")
            print("1. Управление заявками")
            print("2. Оплатить заказ")
            print("3. Добавить...")
            print("0. Выход\n")

            choice = input("Выберите: ")

            if choice == "1":
                manage_order()
            elif choice == "2":
                pay_order()
            elif choice == "3":
                add_smth()

            

            
            elif choice == 0:
                break
            
    finally:
        print('сессия завершена')