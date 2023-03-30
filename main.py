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