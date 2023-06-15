# Множество (set, frozents)
# str, int, bool, list, tuple, float
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# print(set(a + b))
# print(frozenset("fdfdfds"))

# print(set("fdfdfds"))


# st ={'Geeks', 'osh', 'bishkek', 'IT', 'osh'}
# print(st) 
# st.add('Asus')
# print(st)
# st.add('IT')
# print(st)
# st.remove("bishkek")
# print(st)
# st.pop()
# print(st)
# st.clear()          
# print(st)

# Gmails ={'geeks@gmail.com'}
# print(Gmails)
# Gmails.add('Abdullah@gmail.com')
# print(Gmails)
# Gmails.add('Abdullah@gmail.com')
# print(Gmails)
# Gmails.add(1)
# Gmails.add(2)
# print(Gmails)

# Frz = frozenset({1, 2, 3, 4, 5, 6})
# print(Frz)


#словари - dictionary
student = {'name': 'Askhat', 'age' : 19, 'phone_number':996550474345}
print(student)
print(student['name'])
print(len(student))
student.setdefault('language', 'python')
print(student)
student.pop('phone_number')
print(student)
student['age'] = 20
print(student)
print(student.keys())       # Это значение выводит значение ключа
print(student.values())     # Это значение выводит ключ



contact = {'MCHS' :112}
# while True:
#     commands = input(1-посмотреть,2-добавить, 3-удалить, 4-обновить)
#     if  commands == "1":
#         print(contact)
#     elif     commands == "2":
#         add_name = input("имя которую нужно добавить: ")
#         add_number = input("Номер телефона: ")
#         contact.setdefault(add_name, add_number)
#         print(f"Контакт {add_name} успешно добавлен")
#     elif commands == "3":
#         delete_name = input("Имя которую нужна удалить")
#         if delete_name in contact:
#             contact.pop(delete_name)
#             print(f"Контакт {delete_name} успешно удален")
#         else:
#             print("Ттакого контакто нету")
#         elif commands == "4":
#             update_number in contact


