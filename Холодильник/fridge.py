"""
«Холодильник».

Хранит продукты, их количество и сроки годности, позволяет добавлять
продукты, искать их, считать количество и находить просроченные.
"""

from datetime import *
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'  # шаблон даты

goods = {}


def add(items, title, amount, expiration_date=None):
    """
    Добавляет партию продукта в холодильник.

    Args:
        items (dict): Словарь с продуктами (холодильник).
        title (str): Название продукта, оно же ключ в словаре.
        amount (Decimal): Количество продукта.
        expiration_date (str, optional): Срок годности в формате '%Y-%m-%d'.
            По умолчанию None, если срока годности нет.

    Returns:
        None: Функция изменяет словарь items и ничего не возвращает.
    """
    expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date()if expiration_date else None
    if title not in items:
        items[title] = []

    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def add_by_note(items, note):
    """
    Добавляет продукт в холодильник по текстовой информации.

    Информация имеет вид '<название> <количество> <срок годности>'.
    Название может состоять из нескольких слов, а срок годности может
    отсутствовать.

    Args:
        items (dict): Словарь с продуктами (холодильник).
        note (str): Строка с описанием продукта

    Returns:
        None: Функция добавляет продукт в items через add и ничего не
            возвращает.
    """
    words = note.split()
    is_date = False
    # пробую преобразовать дату, если она есть действие выполниться и флаг
    # переключиться, иначе ошибка и флаг false
    try:
        datetime.strptime(words[-1], DATE_FORMAT)
        is_date = True
    except ValueError:
        pass

    if is_date:
        add(items, ' '.join(words[:-2]), Decimal(words[-2]), words[-1])
    else:
        add(items, ' '.join(words[:-1]), Decimal(words[-1]))


def find(items, needle):
    """
    Ищет продукты, в названии которых есть заданная подстрока.

    Поиск не зависит от регистра.

    Args:
        items (dict): Словарь с продуктами (холодильник).
        needle (str): Строка, которую ищем в названиях.

    Returns:
        list: Список названий подходящих продуктов. Если ничего не найдено,
            то возвращается пустой список
    """
    result = []
    for item in items:
        if needle.lower() in item.lower():
            result.append(item)

    return result


def get_amount(items, needle):
    """
    Считает общее количество продукта, название которого было передано.

    Складывает количество всех партий для найденного продукта.

    Args:
        items (dict): Словарь с продуктами (холодильник).
        needle (str): Строка, по которой ищем продукты, регистр при этом не учитывается.

    Returns:
        Decimal: Общее количество. А если ничего не найдется, то вернется 0
    """
    amount = Decimal('0')
    for title in find(items, needle):
        for part in items[title]:
            amount += part['amount']
    return amount


def get_expired(items, in_advance_days=0):
    """
    Находит продукты, у которых срок годности вышел или скоро выйдет.

    Партия подходит, если у неё есть срок годности и он не позже, чем
    сегодня плюс in_advance_days дней. Партии без срока годности вообще не
    учитываются.

    Args:
        items (dict): Словарь с продуктами (холодильник).
        in_advance_days (int, optional): На сколько дней вперёд учитывать
            срок годности.
            По умолчанию 0 - сегодняшная дата будет считаться.

    Returns:
        list: Список кортежей (название, количество)
    """
    result = []
    last_date = date.today() + timedelta(days=in_advance_days)
    for title, parts_item in items.items():
        amount = Decimal('0')
        for part in parts_item:
            if (part['expiration_date'] is not None
                    and part['expiration_date'] <= last_date):
                amount += part['amount']
        if amount > 0:
            result.append((title, amount))
    return result
