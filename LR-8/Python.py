import random
while True:
    print("Попробуйте поймать мячик? ")
    print("Напишите да или нет")
    otvet = input(str)
    if otvet == "да":
    #Ход первый
        shans = random.randint(1, 10)
        if shans < 8:
            print("Мячь пойман ответите на мой вопрос?")
            otvet = input(str)
            if otvet == "да":
                vopros = random.randint(1, 10)
          
                if vopros == 1:
                    print("Как часто вы играете в компьютерные игры?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 2:
                    print("Как часто вы ходите в кино?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 3:
                    print("Как часто вы ходите в зал?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 4:
                    print("У вас есть братья или сестры?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 5:
                    print("Кем вы хотите работать?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 6:
                    print("Как часто вы встречаетесь с друзьями?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 7:
                    print("На сколько хорошо вы знаете английский?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 8:
                    print("Вы смотрите анимэ?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 9:
                    print("Как часто вы пропускаете пары?")
                    otvet = input(str)
                    print("Ответ принят")
                elif vopros == 10:
                    print("Какая музыка вам нравится?")
                    otvet = input(str)
                    print("Ответ принят")
                print("Теперь я ловлю ваш мячик")
                print("Бросить мячик?")
                otvet = input(str)
                if otvet == "да":
                    shans = random.randint(1, 10)
                    if shans < 8:
                        print("Мячь пойман, я отвечу на один ваш вопрос")
                    
                        print("1. Сколько тебе лет?  2. Кого ты не навидешь? 3. Ты учишься? 4. Кто твой лучший друг? 5. Какую ОС предпочитаешь? 6. Как относишься к ядерному оружию? 7. Уступил бы бабушке в автобусе? 8. Какую работу посоветуешь? ")
                        pc = input(str)
                        if pc == "1":
                            print("Мне 47 лет")
                        elif pc == "2": 
                            print("Энекина Скайувокера")
                        elif pc == "3":
                            print("Нет - зачем мне это нужно?!")
                        elif pc == "4":
                            print("Президент Путин")
                        elif pc == "5":
                            print("Конечно же Windows")
                        elif pc == "6":
                            print("Спалил бы вас уже давно")
                        elif pc == "7":
                            print("Ввел бы отдельные автобусы для них, а так нет")
                        elif pc == "8":
                            print("Системный администратор")
                        else:
                            print("Вы указали что-то не так")
                        print("Перейдем дальше?")
                        otvet = input(str)
                        if otvet == "да":
                            print("Хорошо")
                        else:
                            print("Игра окончена")
                            break
                    else:
                        print("Мячь не пойман")
                        print("Перейдем дальше?")
                        otvet = input(str)
                        if otvet == "да":
                            print("Хорошо")
                        else:
                            print("Игра окончена")
                            break
                elif otvet == "нет":
                    print("Игра закончена")
                    break
                else:
                    print("Мячь не пойман, ответите на мой вопрос?")
                    otvet= input(str)
                    if otvet == "да":
                        print("Зачем вы играете в эту игру?")
                        otvet = input(str)
                        print("Ответ принят")
                        print("Перейдем дальше?")
                        otvet = input(str)
                        if otvet == "Да":
                            print("Отлично")
                        else:
                            print("Игра закончена")
                            break
                    else:
                        print("Игра закончена")
                        break

            else:
                print("Игра закончена")
                break
        else:
            print("Мячь не пойман")
            print ("Хотите начать заново?")
            otvet = input(str)
            if otvet == "да":
                print("Начинаем заново")
            else:
                print("Игра закончена")
    elif otvet == "нет":
        print("Жалко")
        break   
    else:
        print("Ну ты и странный!")
        break
