import string
from models.product import Product
from models.product_storage import ProductStorage

from models.common import constant

class App:
    
    def __init__(self) -> None:
        self.running = True
        self.product_storage = ProductStorage()
        pass

    def run(self):
        self.product_storage.read_storage()
        while self.running:
            choice = input('\nЧто вы хотите сделать? (Добавить или посчитать): ').lower().strip()
            self.choose_option(choice)
        pass

    def choose_option(self, choice: str):
        match choice:
            case constant.ADD:
                self.add()
            case constant.CALCULATE:
                self.calculate()
            case _:
                self.close_program()
    
    def add(self):
        name: str = self.__add_input_str('Введите имя продукта')
        description: str = self.__add_input_str('Введите описание продукта')
        calories: float = self.__add_input_float('Введите каллории на 100г продукта')
        carbohydrates: float = self.__add_input_float('Введите углеводы на 100г продукта')
        fats: float = self.__add_input_float('Введите жиры на 100г продукта')
        protein: float = self.__add_input_float('Введите белок на 100г продукта')
        salt: float = self.__add_input_float('Введите соль на 100г продукта')

        self.product_storage.add_product(name, description, calories, carbohydrates, fats, salt, protein)
        return

    def __add_input_str(self, instruction: str) -> str:
        detail = input(f'{instruction}: ').strip().title()
        if detail != '':
            return detail
        else:
            print('Неверно')
            return self.__add_input_str(instruction)

    def __add_input_float(self, instruction: str) -> float:
        try:    
            detail = float(input(f'{instruction}: ').strip().title())
            if detail > 0:
                return detail
            else:
                print('Число должно быть больше 0')
                return self.__add_input_float(instruction)
        except:
            print('Неправильный формат')
            return self.__add_input_float(instruction)


    def calculate(self) -> None:
        product_name = self.__add_input_str('Укажите название продукта')
        product = self.product_storage.find_product(product_name)

        if product == None:
            return
        
        weight = self.__add_input_float('Укажите вес желаемого продукта')
        print(weight)
        calculated_content = product.calculate_product_energy_value(weight)
        print(calculated_content.content_info())
        return

    def close_program(self):
        self.running = False
        return
        
