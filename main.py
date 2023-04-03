#Задание 2.
#Реализуйте класс «Стадион». Необходимо хранить в полях класса:
#название стадиона, дату открытия, страну, город, вместимость. Реализуйте
#конструктор по умолчанию и метод для вывода данных.
class Stadium:
    name: str
    opening_date: Dict[str, str]
    country: str
    city: str
    capacity: int

    def __init__(self, name: str, opening_date: Dict[str, str], country: str, city:str, capacity: int):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Название: {self.name}\n"\
               f"Дата открытия:{self.opening_date}\n"\
               f"Страна: {self.country}\n"\
               f"Город:{self.city}\n"\
               f"Вместимость:{self.capacity}\n"

def execute_application():


    # Задание 2.
    stadium = Stadium('Шинник', {'день': '01', 'месяц': '01', 'год': '1957'}, 'Россия', 'Ярославль', 22990)
    print(stadium)
if __name__=="__main__":
    execute_application()
