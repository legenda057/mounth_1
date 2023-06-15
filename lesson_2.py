# print("hello Geeks and Python") # Выводит слово
# """ 



#str_example_1 = 'Hello, I\'m backend developer' 
#print(str_example_1)

# str_example_2 = "Hello, I'm backend developer \n Language Python "
# print(str_example_2)

# str_example_3 = """ Hello, I'm backend developer 
# language pytthon  """ 
# print(str_example_3)

# str_example_4 = ''' hello , i'm backend developer 
# Language Python '''
# print(str_example_4)

# конкантенация - это склеивание строк через оператор +
# print("Nurbolot" + " " + 'Erkinbaev')
# print("Nurbolot" + "Erkinbaev")


# name = input ("Имя: ")
# print("Привет" , name)

it = "Geeks " #Индекс строк 
      #01234
print (it[3])
print(it[0])
print(it[5])

# print(it[0:3])

# language = "Python"
#             #0123456
# print(language [0:2])
# print(language [::2])

# name = "nurBoLot"
# print(name.title())
# print(name.upper())
# print(name .lower())  

#условие if , elif , else 
# num1 = 31 
# num2 = 32

# if num1 > num2: 
#     print("переменная num1 больше")
# elif num1 ==num2:
#     print("num1 равен num2")
# else:
#     print("переменная num2 больше")

# операторы сравнение (6)
# print(30==30)
# print(40==10)

# print(20 != 5)
# print(10 != 10)

# print(30 > 3)
# print(30 > 100)

# print(40 < 4)
# print(40 <= 40)

# print(40 <= 100)
# print(50>= 100)

# print(60 >=60)

age = int(input("ваш возрас: "))
if age < 14 : 
    print("Извините , ваш возраст не подходит ")
else:
    print("Добро пожаловать на курсы Geeks")

login = input("login: ")
password = input("password: ")
if login == "geeks" or password == "geeksstudents":
    print("Welcome")
else:
    print("Error")


if num1> num2 and num1 > num3 :
    print('num1 болбше')
elif num2 > num1 and num2 > num3 :
    print('num2 болбше')
else:
    print("num3 больше")
    