# Задание №1

with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    ingredients_list = []
    for line in f:
        dish_name = (line.strip())
        ingredients_quantity = int(f.readline().strip())
        for ingr in range(ingredients_quantity):
            ingredients_dict = {}
            ingredients = (f.readline().split(' | '))
            ingredients_dict['ingredient_name'] = ingredients[0]
            ingredients_dict['quantity'] = ingredients[1]
            ingredients_dict['measure'] = ingredients[2]
            ingredients_list.append(ingredients_dict)
            cook_book[dish_name] = ingredients_list
        f.readline().strip()


# print(cook_book)

# Задание №2


def get_shop_list_by_dishes(dishes, person_count):
    info_ingredients_dict = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            amount = ingredient['quantity'] * person_count
            un = ingredient['measure']
            name = ingredient['ingredient_name']
            if name not in info_ingredients_dict:
                info_ingredients_dict[name] = {'measure': un, 'quantity': amount}
            else:
                info_ingredients_dict[name]['quantity'] += amount
    return info_ingredients_dict


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задание №3
import os

dict_ = {}
for filename in os.listdir():
    if ".txt" in filename:
        with open(os.path.join(filename), "r", encoding="utf-8") as f:
            text = f.readlines()
            len_ = len(text)
            dict_[filename] = {"lines": len_, "text": text}
# print(dict_)

with open('4.txt', 'w', encoding='utf-8') as f:
    for key, value in dict_.items():
        f.write(f" {key}, \n")
        f.write(f" {str(value['lines'])} \n")
        f.write(f""" {str(" ".join(value['text']))} \n""")


