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



def execute_application():
    pass





if __name__=="__main__":
    execute_application()