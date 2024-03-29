# Здесь класс который будет описывать доход организции

# Определяет статьи доходов 
#           наименование (словарь где ключ это название, а значение это список примерных названий, то как можно их назвать голосом или текстом)

# Класс принимает сообщение из init, 
    # дальше ищет соответствие в базе данных 
    # и вставляет запись в соответствующую таблицу БД

from project_basis.badget import Badget


class Income(Badget):
        
    income_item = {
        'sale_capital_assets':[],           # - доходы от продажи основных средств
        'sale_product':[],                  # - доходы от продажи товара
        'sale_service':[],                  # - доходы за оказание услуг
        'investment':[],                    # - инвестиции
        'credit':[],                        # - кредититование
        'rent':[],                          # - аренда (техники, имущества, зданий и сооружений)
        'currency':[],                      # - операции с валютой (скальпинг возможно)
        'other_sales':[]                    # - прочее
    }

    def __init__(self, item: dict) -> dict:
        super().__init__(item)
        self.income_item = item

