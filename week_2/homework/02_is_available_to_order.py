# .sort()  함수를 적극 이용하자
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# set이라는 집합 자료구조형을 이용해 구하자.(중복되는 원소는 없애고 하나만 들어가는 자료형이다.)
def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)