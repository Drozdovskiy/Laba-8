import random
print('Выберите дверь\n1 2 3')
otvet =  int(input())
pc = random.randint(1,3)
print(f'Другой игрок выбрал {pc}')
chance = random.randint(1,3)
while True:
    if (chance != otvet) and (chance != pc):       
        print(f'За дверью {chance} пусто')
        print("Хотите ли вы изменить свой выбор?")
        otvet1 = str(input())
        if otvet1 == "да": 
            print(f"Выберите одну из дверей, кроме двери {chance}")
            otvet = int(input())
            pc = pc
            chansdoor = random.randint(1, 10)
            if chansdoor < 6:
                print(f"За дверью {otvet} приз, вы выйграли")
                if otvet != pc:
                    print(f"За дверью {pc} пусто")
                    break
                elif otvet == pc:
                    print("Ваш соперник тоже угадал")
                    break
            elif chansdoor > 5:
                print(f"За дверью {otvet} пусто, вы проиграли") 
                if otvet != pc:
                    print(f"Приз за {pc} дверью, вы проиграли")
                    break
                elif otvet == pc:
                    print(f"Вы оба проиграли")
                    break
        elif otvet1 == "нет":
            pcdoor = random.randint(1, 2)
            door1 = random.randint(1, 2)
            if door1 == 1:
                print(f"За дверью {otvet} приз, вы выйграли")
                if otvet != pc:
                    print(f"За дверью {pc} пусто")
                    break
                elif otvet == pc:
                    print("Ваш соперник тоже угадал")
                    break

            else:
                print(f"За дверью {otvet} пусто, вы проиграли") 
                if otvet != pc:
                    print(f"За дверью {pc} приз")
                    break
                elif otvet == pc:
                    print(f"Вашь соперник тоже не угадал")
                    break
    else:
        chance = random.randint(1,3)
