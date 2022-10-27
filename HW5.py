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

info = """p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
имя владельца и номер полки, на котором он будет храниться.
"""


def people(user_num):
    for vocs in documents:
        if user_num == vocs["number"]:
            return vocs['name']


def shelf(user_num):
    for index, numbers in enumerate(directories.values()):
        if user_num in numbers:
            return index + 1
    else:
        result = "Такого документа нет"
        return result


def to_list():
    for vocs in documents:
        return f' {vocs["type"]} "{vocs["number"]}" "{vocs["name"]}"'


def add(type_, number, name, shelf_num):
    if int(shelf_num) > 3 or int(shelf_num) < 1:
        return "Такой полки нет"
    else:
        new_voc = {"type": type_, "number": number, "name": name}
        documents.append(new_voc)
        for key, value in directories.items():
            if shelf_num == key:
                value.append(number)
        return "Данные добавлены"


def delete_document(doc_num):
    document = doc_num
    for key, value in directories.items():
        if document in value:
            value.remove(document)
    for doc in documents:
        if document in doc['number']:
            documents.remove(doc)
            return f'Документ {document} удален'
    return 'Такого документа не существует'


def run():
    print(info)
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
        elif command == "d":
            user_num = input("Какой номер документа? ")
            delete_document(user_num)
        elif command == "a":
            type_ = input("Какой тип документа: ")
            number = input("Какой номер документа: ")
            name = input("Имя владельца: ")
            shelf_num = input("Номер полки: ")
            add(type_, number, name, shelf_num)
        else:
            print("Повторите попытку")



if __name__ == "__main__":
    run()
