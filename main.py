
class HotDog:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients


class HotDogStand:
    def __init__(self):
        self.hot_dogs_list = []
        self.ingredients_dict = {}
        self.sales = {'Наличка': [], 'Карта': []}

    def add_hot_dog(self, hot_dog):
        self.hot_dogs_list.append(hot_dog)

    def remove_hot_dog(self, hot_dog_name):
        for hot_dog in self.hot_dogs_list:
            if hot_dog.name == hot_dog_name:
                self.hot_dogs_list.remove(hot_dog)

    def add_ingredient(self, ingredient, quantity):
        if ingredient in self.ingredients_dict:
            self.ingredients_dict[ingredient] += quantity
        else:
            self.ingredients_dict[ingredient] = quantity

    def remove_ingredient(self, ingredient, quantity):
        if ingredient in self.ingredients_dict:
            if self.ingredients_dict[ingredient] >= quantity:
                self.ingredients_dict[ingredient] -= quantity
            else:
                print(f"Недостаточно {ingredient} для удаления.")
        else:
            print(f"{ingredient} нет в наличии.")

    def create_hot_dog(self, hot_dog_name, ingredients):
        hot_dog = HotDog(hot_dog_name, sum([ingredient.price for ingredient in ingredients]), ingredients)
        self.add_hot_dog(hot_dog)
        print(f"{hot_dog_name} создан успешно.")

    def display_hot_dogs(self):
        if len(self.hot_dogs_list) == 0:
            print("Хот-догов нет в наличии.")
        else:
            print("Доступные хот-доги: ")
            for hot_dog in self.hot_dogs_list:
                ingredients = ", ".join([ingredient.name for ingredient in hot_dog.ingredients])
                print(f"{hot_dog.name} ({ingredients}): {hot_dog.price}")

    def display_ingredients(self):
        if len(self.ingredients_dict) == 0:
            print("В наличии нет ингридиентов.")
        else:
            print("Доступные ингридиенты:")
            for ingredient, quantity in self.ingredients_dict.items():
                print(f"{ingredient}: {quantity}")

    def sell_hot_dog(self, hot_dog_name, payment_type):
        for hot_dog in self.hot_dogs_list:
            if hot_dog.name == hot_dog_name:
                if payment_type == 'наличка':
                    self.sales['наличка'].append(hot_dog.price)
                elif payment_type == 'карта':
                    self.sales['карта'].append(hot_dog.price)
                else:
                    print(f"Некорректный метод оплаты: {payment_type}.")
                    return
                self.remove_hot_dog(hot_dog_name)
                print(f"{hot_dog_name} продан за {hot_dog.price} {payment_type}.")
                return
        print(f"{hot_dog_name} нет в наличии.")

    def calculate_discount(self, num_hot_dogs):
        if num_hot_dogs >= 3:
            return 0.1
        else:
            return 0

    def calculate_revenue(self):
        revenue = sum(self.sales['наличка']) + sum(self.sales['карта'])
        return revenue

    def calculate_profit(self, cost):
        revenue = self.calculate_revenue()
        profit = revenue - cost
        return profit

    def display_statistics(self, cost):
        num_hot_dogs_sold = len(self.sales['наличка']) + len(self.sales['карта'])
        revenue = self.calculate_revenue()
        profit = self.calculate_profit(cost)
        print(f"Кол-во проданных хот-догов: {num_hot_dogs_sold}")
        print(f"Доход: {revenue}")
        print(f"Общая прибыль: {profit}")

        with open('checker.txt', 'w') as f:
            f.writelines(f'Кол-во проданных хот-догов: {num_hot_dogs_sold}')
            f.writelines(f'Доход: {revenue}')
            f.writelines(f'Общая прибыль: {profit}')
            f.close()


    def check_ingredients_stock(self, hot_dog):
        for ingredient in hot_dog.ingredients:
            if ingredient.name not in self.ingredients_dict or self.ingredients_dict[ingredient.name] <= 0:
                print(f"Недостаточно {ingredient.name} для создания {hot_dog.name}. Закажите {ingredient.name}.")
                return False
        return True

    def order_more_ingredients(self, ingredient, quantity):
        print(f"{quantity} больше {ingredient} заказа.")


class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class HotDogRecipe:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)


def main():
    hot_dog_stand = HotDogStand()
    hot_dog_stand.add_ingredient("Булочки для хот-догов", 200)
    hot_dog_stand.add_ingredient("Хот-доги", 100)
    hot_dog_stand.add_ingredient("Майонез", 50)
    hot_dog_stand.add_ingredient("Кетчуп", 50)
    hot_dog_stand.add_ingredient("Горчица", 50)
    hot_dog_stand.add_ingredient("Луковый соус", 50)
    hot_dog_stand.add_ingredient("Халапеньо", 50)
    hot_dog_stand.add_ingredient("Чили", 50)
    hot_dog_stand.add_ingredient("Маринованые огурцы", 50)

    hot_dog_recipe_1 = HotDogRecipe()
    hot_dog_recipe_1.add_ingredient(Ingredient("Булочки для хот-догов", 2))
    hot_dog_recipe_1.add_ingredient(Ingredient("Хот-дог", 4))
    hot_dog_recipe_1.add_ingredient(Ingredient("Кетчуп", 1))
    hot_dog_recipe_1.add_ingredient(Ingredient("Маринованые огурцы", 1))
    hot_dog_stand.create_hot_dog("Классический хот-дог", hot_dog_recipe_1.ingredients)

    hot_dog_recipe_2 = HotDogRecipe()
    hot_dog_recipe_2.add_ingredient(Ingredient("Булочки для хот-догов", 2))
    hot_dog_recipe_2.add_ingredient(Ingredient("Хот-дог", 4))
    hot_dog_recipe_2.add_ingredient(Ingredient("Майонез", 1))
    hot_dog_recipe_2.add_ingredient(Ingredient("Кетчуп", 1))
    hot_dog_stand.create_hot_dog("Кетчунезный хот-дог", hot_dog_recipe_2.ingredients)

    hot_dog_recipe_3 = HotDogRecipe()
    hot_dog_recipe_3.add_ingredient(Ingredient("Булочки для хот-догов", 2))
    hot_dog_recipe_3.add_ingredient(Ingredient("Хот-дог", 4))
    hot_dog_recipe_3.add_ingredient(Ingredient("Чили", 2))
    hot_dog_recipe_3.add_ingredient(Ingredient("Луковый соус", 2))
    hot_dog_stand.create_hot_dog("Чили хот-дог", hot_dog_recipe_3.ingredients)

    while True:
        print("1. Создать собственный рецепт хот дога")
        print("2. Доступные хот-доги")
        print("3. Доступные ингридиенты")
        print("4. Купить хот-дог")
        print("5. Отобразить статистику продаж")
        print("0. Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            hot_dog_recipe = HotDogRecipe()
            hot_dog_name = input("Введите название для вашего хот-дога: ")
            while True:
                ingredient_name = input("Введите название ингридиента (введите 'готово', когда закончите): ")
                if ingredient_name.lower() == 'готово':
                    break
                ingredient_price = input("Введите цену ингридиента: ")
                hot_dog_recipe.add_ingredient(Ingredient(ingredient_name, int(ingredient_price)))
                hot_dog_stand.create_hot_dog(hot_dog_name, hot_dog_recipe.ingredients)
        elif choice == "2":
            hot_dog_stand.display_hot_dogs()
        elif choice == "3":
            hot_dog_stand.display_ingredients()
        elif choice == "4":
            while True:
                hot_dog_name = input("Введите название хот-дога: ")
                payment_type = input("Выберите тип оплаты (наличка или карта):")
                hot_dog = None
                for hot_dog in hot_dog_stand.hot_dogs_list:
                    if hot_dog.name == hot_dog_name:
                        break
                if hot_dog:
                    if hot_dog_stand.check_ingredients_stock(hot_dog):
                        hot_dog_stand.sell_hot_dog(hot_dog_name, payment_type)
                        break
                else:
                    print(f"Хот-догов с названием {hot_dog_name} не найдено.")
        elif choice == "5":
            hot_dog_cost = sum([hot_dog.price for hot_dog in hot_dog_stand.hot_dogs_list]) / len(hot_dog_stand.hot_dogs_list)
            hot_dog_stand.display_statistics(hot_dog_cost)
        elif choice == "0":
            break
        else:
            print("Некорректный ввод!!!!!!.")

if __name__ == "__main__":
    main()