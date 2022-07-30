documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.


def people(user_num):
    for vocs in documents:
        if user_num == vocs["number"]:
            print(vocs['name'])


def shelf(user_num):
    for id, numbers in enumerate(directories.values()):
        if user_num in numbers:
            print(id + 1)
    else:
        print("Такого документа нет")
        return


def to_list():
    for vocs in documents:
        print(f' {vocs["type"]} "{vocs["number"]}" "{vocs["name"]}"')


def add(type, number, name, shelf_num):
    if int(shelf_num) > 3 or int(shelf_num) < 1:
        print("Такой полки нет")
    else:
        new_voc = {"type": type, "number": number, "name": name}
        documents.append(new_voc)
        print("Данные добавлены")
        directories[shelf_num].append(number)


while True:
    command = input("Введите команду: ")
    if command == "p":
        user_num = input("Какой номер документа? ")
        people(user_num)
    elif command == "s":
        user_num = input("Какой номер документа? ")
        shelf(user_num)
    elif command == "l":
        to_list()
    elif command == "a":
        type = input("Какой тип документа: ")
        number = input("Какой номер документа: ")
        name = input("Имя владельца: ")
        shelf_num = input("Номер полки: ")
        add(type, number, name, shelf_num)
    else:
        print("Повторите попытку")
