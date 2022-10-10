# Задание № 1

# print("""Добро пожаловать в ипотечный калькулятор, пожалуйста пройдите краткий опрос для получения ипотечной ставки,
#       Напишите "Да" или "Нет" """)
#
# start_morgage = 10
# discount_salary = 0
# discount_child = 0
# discount_insurance = 0
#
# region_client = input("Вы проживаете в Центральном Казахстане? Да/Нет ")
#
#
# if region_client == "Да":
#   final_morgage = 2
#   print("Ваша ставка:", final_morgage, "%")
# else:
#   salary_client = input("Вы получаете зарплату в нашем банке? Да/Нет ")
#   child_client = input("У вас в семье детей 3 и более? Да/Нет ")
#   insurance_client = input("Оформлено ли у Вас страхование в нашем банке? Да/Нет ")
#   final_morgage = start_morgage
#   if salary_client == "Да":
#     discount_salary += 1
#   if child_client == "Да":
#     discount_child += 0.5
#   if insurance_client == "Да":
#     discount_insurance += 1.5
#   print("Ваша ставка:", final_morgage - discount_child - discount_insurance - discount_salary, "%")

  


  
# Задание № 2

month = input("Введите месяц рождения: ")
day = int(input("Введите день рождения: "))

if month == "март" and day >= 21 or month == "апрель" and day <= 20:
  print("Овен")
elif month == "апрель" and day >= 21 or month == "май" and day <= 21:
  print("Телец")
elif month == "май" and day >= 22 or month == "июнь" and day <= 21:
  print("Близнецы")
elif month == "июнь" and day >= 21 or month == "июль" and day <= 20:
  print("Рак")
elif month == "июль" and day >= 23 or month == "август" and day <= 23:
  print("Лев")
elif month == "август" and day >= 24 or month == "сентябрь" and day <= 23:
  print("Дева")
elif month == "сентябрь" and day >= 24 or month == "октябрь" and day <= 23:
   print("Весы")
elif month == "октябрь" and day >= 24 or month == "ноябрь" and day <= 22:
  print("Скорпион")
elif month == "ноябрь" and day >= 23 or month == "декабрь" and day <= 21:
  print("Стрелец")
elif month == "декабрь" and day >= 22 or month == "январь" and day <= 20:
  print("Козерог")
elif month == "январь" and day >= 21 or month == "февраль" and day <= 18:
  print("Водолей")
elif month == "февраль" and day >= 19 or month == "март" and day <= 20:
  print("Рыбы")