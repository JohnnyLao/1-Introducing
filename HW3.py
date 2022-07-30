# ЗАДАНИЕ № 1

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

run = 1
while run:
  
  command = input("Введите 'start'- для начала, 'exit' - для выхода, 'add' - чтобы добавить имя: ")
  if command == 'start':
   if len(boys) > len(girls):
     print("Недостаточно девушек")
   elif len(boys) < len(girls):
     print("Недостаточно парней")
   else:
    boys_and_girls = zip(sorted(boys), sorted(girls))
    print("Идеальные пары:")
    for boy, girl in list(boys_and_girls):
      print(f"{boy} и {girl}")
  
  elif command == 'exit':
    run = 0
    print("До свидания!")
  
  elif command == "add":
    gender = input("Введите пол: male/female: ")
    if gender == "male":
      name_male = input("Введите Имя: ")
      boys.append(name_male)
      print(f"{name_male} добавлен в мужской список")
    elif gender == "female":
      name_female = input("Введите Имя: ")
      girls.append(name_female)
      print(f"{name_female} добавлена в женский список")
    else:
      print("Неизвестная команда, попробуйте еще раз")
  else:
    print("Неизвестная команда, попробуйте еще раз")


# ЗАДАНИЕ № 2

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]


run = 1
while run:
  
  persons = int(input("На сколько человек необходимо расчитать ингредиенты: "))
 
  print(f"Для приготовления на {persons}-х человек, необходимо:")
  
  for dish, list in cook_book:
    print()
    print(f"{dish.capitalize()}:")
    for ingredient, quantity, size in list:
      print(ingredient, str(quantity * persons) + size)    # В задании нет пробела между цифрой и ед.измерения, если так то придется сделать строчку из цифры, в обычном порядке будет пробел)