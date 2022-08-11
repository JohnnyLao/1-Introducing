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

# Задание №2

files_dict = {}
files_text = {}
with open("3.txt", encoding='utf-8') as f:
    for quantity, line in enumerate(f):
        files_dict['3.txt'] = quantity + 1
        files_text['3.txt'] = line

with open("2.txt", encoding='utf-8') as f:
    for quantity, line in enumerate(f):
        files_dict['2.txt'] = quantity + 1
        files_text['2.txt'] = line
with open("1.txt", encoding='utf-8') as f:
    for quantity, line in enumerate(f):
        files_dict['1.txt'] = quantity + 1
        files_text['1.txt'] = line
line = 0
for lines in files_dict.values():
    if lines > line:
        line = lines
    else:
        pass

with open('4.txt', 'w', encoding='utf-8') as f:
    for file, lines in files_dict.items():
        if lines == line:
            f.write(file.strip())
            f.write("\n")
            f.write(str(lines))
            f.write("\n")
            f.write(files_text[file])


# print(files_dict)