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
        print("Name:", self.name)
        print("Opening date:", self.opening_date)
        print("Country:", self.country)
        print("City:", self.city)
        print("Capacity:", self.capacity)



def execute_application():
    # Задание 2.
    car1 = Car('Sorento', 2021, 'KIA', 2.5, 'красный', 4079900)
    car1.display_info()





if __name__=="__main__":
    execute_application()