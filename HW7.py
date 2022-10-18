# Задание №1
from pprint import pprint
cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        dish_name = (line.strip())
        ingredients_quantity = (f.readline().strip())
        ingredients_list = []
        for ingr in range(int(ingredients_quantity)):
            ingredients_dict = {}
            ingredient_name, quantity, measure = f.readline().split('|')
            ingredients_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        cook_book[dish_name] = ingredients_list
        f.readline()
    # pprint(cook_book)


# Задание №2


def get_shop_list_by_dishes(dishes, person_count):
    info_ingredients_dict = {}
    for dish in dishes:
        if dish not in cook_book.keys():
            result = 'Такого блюда в книге нет!'
            return result
        else:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                amount = int(ingredient['quantity']) * person_count
                un = ingredient['measure']
                name = ingredient['ingredient_name']
                if name not in info_ingredients_dict:
                    info_ingredients_dict[name] = {'measure': un, 'quantity': amount}
                else:
                    info_ingredients_dict[name]['quantity'] += amount
    pprint(info_ingredients_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 10)

# Задание №3
import os

data = {}
files_list = []


for filename in os.listdir():
    if ".txt" in filename:
        files_list.append(filename)
        with open(os.path.join(filename), "r", encoding="utf-8") as f:
            text = f.readlines()
            len_ = len(text)
            data[len_] = {"File": filename, "text": text}
            data = dict(sorted(data.items()))


with open('Result.txt', 'w', encoding='utf-8') as f:
    for key, value in data.items():
        f.write(f" {key}, \n")
        f.write(f" {str(value['File'])} \n")
        f.write(f""" {str(" ".join(value['text']))} \n""")

pprint(data) # Check