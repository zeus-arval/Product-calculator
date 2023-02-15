class ProductContent:
    def __init__(self, calories: float, carbohydrates: float, fats: float, protein: float, salt: float) -> None:
        self.calories = calories / 100
        self.carbohydrates = carbohydrates / 100
        self.fats = fats / 100
        self.protein = protein / 100
        self.salt = salt / 100
        pass
    
    def content_info(self) -> str:
        return str(f'Калории: {self.calories}\n'
                   f'Углеводы: {self.carbohydrates}\n'
                   f'Жиры: {self.fats}'
                   f'Белок: {self.protein}\n'
                   f'Соль: {self.salt}')

    def as_string(self) -> str:
        return str(f'{self.calories},{self.carbohydrates},{self.fats},{self.protein},{self.salt}')