# def calculator() :
#     num1 = int(input("number1: "))
# operator = input("+, -, *, /,: ")
# num2 = int(input("number2: "))
# if operator == "+" :
#     print(f"Result {num1 + num2}")
# elif operator == "-" :
#     print(f"Result {num1 - num2}")
# elif operator == "*" :
#     print(f"Result {num1 * num2}")
# elif operator == "/" :
#     print(f"Result {num1 / num2}")
# else:
#     print("Error operator")

# def add(num1, num2) :   # num1 ,  num2 является переменами  функцией add
#     print(num1 + num2)
# add(10, 20)
# add("10", "20")

# def mult(num1:int, num2:int):
#     print(num1 * num2)
# mult("Geeks", 3) #
# mult(10, 20)

# def sub(num1: int, num2:int) -> int :
#     print(num1 - num2)
# sub(20, 10)

# def div(num1:int=1, num2:int=1) -> float :
#     "данная функция принимает две числа и делит их"
#     print(num1 / num2)
#     div(400, 2)
#     div(20)

# import random

# def generate_password(len_password:int(=8))-> str:
# letters = "qwertyuiopasdfghpjklzxcvbnm1234567890"
# resylt = ""
# for n in range(8):
#         random_letters = random.choice(letters)
#         result += random_letters
# print(random)

#исключеник try, except
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Yа ноль делить нельзя!")


# def calculator(num1:int=1, operator:str="+", num2:int=1):
#     try:
#         if operator == "+":
#             print(f"Result {num1 + num2}")
#         elif operator == "-":
#             print(f"Result {num1 - num2}")
#         elif operator == "*":
#             print(f"Result {num1 * num2}")
#         elif operator == "/":
#             try:
#                 print(f"Result {num1 / num2}")
#             except ZeroDivisionError:
#                 print("Деление на ноль!")
#             except TypeError:
#                 print("Ошибка деления проверьте что num1 и num2 integer")
#         else:
#             print("Error operator")
#     except TypeError:
#         print("Ошибка")
# calculator(20, "+", 20)
# calculator(10, "/", 0)
# calculator("Hello", "-", "World")

# ralse ValuError("Hello Geeks")
