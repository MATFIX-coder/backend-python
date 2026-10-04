def print_pack_report(count):
    for i in range(count, 0, -1):
        if all(i % x == 0 for x in [3, 5]):
            print(f"{i} - расфасуем по 3 или по 5")
        elif i % 3 == 0 and i % 5 != 0:
            print(f"{i} - расфасуем по 3")
        elif i % 3 != 0 and i % 5 == 0:
            print(f"{i} - расфасуем по 5")
        else:
            print(f"{i} - не заказываем!")

