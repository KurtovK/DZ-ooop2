#Задание 1.
#Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
#название модели, год выпуска, производителя, объем двигателя, цвет машины,
#цену. Реализуйте конструктор по умолчанию и метод для вывода данных.
class Car:
    def __init__(self, model='', year=0, manufacturer='', engine_volume=0, color='', price=0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def display_info(self):
        print('Модель:', self.model)
        print('Год выпуска:', self.year)
        print('Производитель:', self.manufacturer)
        print('Объем двигателя:', self.engine_volume)
        print('Цвет машины:', self.color)
        print('Цена:', self.price)




#Задание 2.
#Реализуйте класс «Стадион». Необходимо хранить в полях класса:
#название стадиона, дату открытия, страну, город, вместимость. Реализуйте
#конструктор по умолчанию и метод для вывода данных.
class Stadium:
    def __init__(self):
        self.name = ""
        self.opening_date = ""
        self.country = ""
        self.city = ""
        self.capacity = 0

    def display_info(self):
        print("Название:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Вместимость:", self.capacity)



def execute_application():

    # Задание 1.
    car1 = Car('Sorento', 2021, 'KIA', 2.5, 'красный', 4079900)
    car1.display_info()


    # Задание 2.
    stadium = Stadium()
    stadium.name = "Шинник"
    stadium.opening_date = "1957"
    stadium.country = "Россия"
    stadium.city = "Ярослалвь"
    stadium.capacity = 22990

    stadium.display_info()





if __name__=="__main__":
    execute_application()