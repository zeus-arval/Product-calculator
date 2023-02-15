from models.product import Product

class ProductStorage:
    def __init__(self) -> None:
        self.__products: list[Product] = []
        self.__products_storage_path = './products.txt'
        pass

    def add_product(self, name: str, description: str, calories: float, carbohydrates: float, fats: float, salt: float,
                    protein: float) -> None:
        product = Product(name, description, calories, carbohydrates, fats, protein, salt)

        try:
            with open(self.__products_storage_path, 'a', encoding='utf-8') as writer:
                print(product.as_string())
                writer.write(product.as_string())
            self.__products.append(product)
            print('Продукт успешно добавлен!')
        except:
            print('Не удалось добавить продукт')
        pass

    def find_product(self, product_name: str) -> Product:
        for product in self.__products:
            if product.get_name() == product_name:
                return product

        print('Такого продукта нет')
        return None

    # Читает файл при запуске программы
    def read_storage(self) -> None:
        try:
            reader = open(self.__products_storage_path, 'r', encoding='utf-8')
            for line in reader:
                product = self.__try_convert_line_to_product(line)
                self.__products.append(product)

            reader.close()
        except:
            print('не удалось прочитать файл с продуктами')
        pass

    @staticmethod
    def __try_convert_line_to_product(line: str) -> Product:
        product_details = line.split(',')

        if len(product_details) == 7:
            try:
                product = Product(product_details[0],
                                  product_details[1],
                                  float(product_details[2]),
                                  float(product_details[3]),
                                  float(product_details[4]),
                                  float(product_details[5]),
                                  float(product_details[6]))

                return product
            except:
                print('Invalid format of data')

        return None
