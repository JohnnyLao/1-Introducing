print("ЗАДАНИЕ № 1")

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

print("""Визиты в Россию:
      """)

for vocabulary in geo_logs:
   for list1 in vocabulary.values():
     for city in list1:
      if "Россия" == city:
        print(vocabulary)



print()
print("ЗАДАНИЕ № 2")

numbers_list = []

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
for numbers in ids.values():
  numbers_list.extend(numbers)

a = (set(numbers_list))
print(list(a))          


  


print()
print("ЗАДАНИЕ № 3")
  
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

total_searches = len(queries)
freqs = {}

for q in queries:
  wlen = len(q.split(" "))
  freqs[wlen] = freqs.get(wlen, 0) + 1

for words, numbers in freqs.items():
  print(f'Поисковых запросов из {words} слов(а) {int(numbers / total_searches * 100)}%')

  


print()
print("ЗАДАНИЕ № 4")
   
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_count = 0
max_id = None
count = (list(stats.values()))

for id, number in enumerate(count):
  if number > max_count:
    max_count = number
    max_id = id

print(f'Больше всего объёма у {list(stats)[max_id].capitalize()}, {max_count}')