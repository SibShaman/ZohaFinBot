from abc import ABC


class Badget(ABC):
  
    # конструктор класса - определяем словарь
    def __init__(self, item: dict, ) -> dict:
        self.item = item


    # получает значение от бота (id пользователя, количество денег, статья доходов, наименование проекта, текст описание, дата записи)
    def get_message():
        pass

    # сравнивает описание со значениями в словаре
    def compare_value():
        pass

    # отправляет сумму и описание в соответствующую таблицу БД, где название таблицы совпадает с ключом статьи дохода
    def add_value_db():
        pass

    # проверка появления записи в БД
    def check_record_db():
        pass
