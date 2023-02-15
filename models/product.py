from itertools import product
from unicodedata import name
from models.product_content import ProductContent


class Product:
    def __init__(self, name: str, description: str, calories: float, carbohydrates: float, fats: float, protein: float, salt: float) -> None:
        self.name = name
        self.description = description
        self.product_content = ProductContent(calories, carbohydrates, fats, protein, salt)
        pass

    def get_name(self) -> str:
        return self.name

    def print_product_info(self) -> None:
        product_content = self.product_content.content_info()
        print(f'Название продукта: {self.name}\n'
              f'Описание: {self.description}\n' +
              product_content)
        pass

    def calculate_product_energy_value(self, weight: float) -> ProductContent:
        calories = self.product_content.calories * weight
        carbohydrates = self.product_content.carbohydrates * weight
        fats = self.product_content.fats * weight
        protein = self.product_content.protein * weight
        salt = self.product_content.salt * weight
        print(weight, calories, self.product_content.calories)
        return ProductContent(calories, carbohydrates, fats, protein, salt) 

    def as_string(self) -> str:
        return f'{self.name},{self.description},{self.product_content.as_string()}'

