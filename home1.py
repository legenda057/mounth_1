

def rus():
    rus_2 = input("Введите фразу: ")

    rus_3 = rus_2.split(' ')

    rus_4 =''.join(i[0].upper() for i in rus_3 )

    print(rus_4)



def lip():
    texs = input ("Введите текст: ").split()
    liste = {}
    for i in texs:
        cnt = texs.count(i)
        liste[i] = cnt
    print(liste)
lip()


# def f():  # 3 Задание
#     fh = input("Введите слово: ")
#     pr = set(fh.lower())
#     for i in fh:
#         if fh.count(i) > 1:
#             print(False)
#             break
#         else:
#             print(True)
#             break
# f()

# def ji(n):   #4 задание
#     pt = 0
#     while n > 0 :
#         pt = pt * 10 + n %10
#         n //= 10
#         print(pt)
# n = 27
# ji(n)



# def chat_bot():
#     while True:
#         user_input = input("Ваш вопрос или команда: ")
#         if user_input.isupper():
#             print("Успокойся")
#             continue
#         if len(user_input) >= 1:
#             print("Конечно")
#             continue
#         elif not user_input:
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("Ну и что")
# chat_bot()





