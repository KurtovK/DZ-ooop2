from typing import Dict
#Задание 1.
#Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
#название модели, год выпуска, производителя, объем двигателя, цвет машины,
#цену. Реализуйте конструктор по умолчанию и метод для вывода данных.
class Car:
    model: str
    year: int
    manufacturer: str
    engine_volume: float
    color: str
    price: float
    def __init__(self, model: str, year: int,manufacturer: str,
                 engine_volume: float, color: str, price: float):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.price = price


    def __str__(self):
        return f"Модель: {self.model}\n" \
               f"Год выпуска: {self.year}\n" \
               f"Производитель: {self.manufacturer}\n"\
               f"Объем двигателя: {self.engine_volume}\n" \
               f"Цвет машины: {self.color}\n" \
               f"Цена: {self.price}\n"




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
    # Задание 1.
    car1 = Car('Sorento', 2021, 'KIA', 2.5, 'красный', 4079900)
    print(car1)
    print()

    # Задание 2.
    stadium = Stadium('Шинник', {'день': '01', 'месяц': '01', 'год': '1957'}, 'Россия', 'Ярославль', 22990)
    print(stadium)
if __name__=="__main__":
    execute_application()
