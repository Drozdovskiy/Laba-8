import random
common = 0
pccommon = 0
rare = 0
pcrare = 0
epic = 0
pcepic = 0
pcrare = 0
legendary = 0
pclegendary = 0
item = 0

for _ in range(0, 21):
    shans = random.random() 
    
    if shans > 0.20 and shans <= 0.70:
        common += 1
        print("\033[32;1mОбычный\033[m")
    elif shans <= 0.20 and shans > 0.10:
        rare += 1
        print("\033[94;1mРедкий\033[m")
    elif shans <= 0.10 and shans > 0.05:
        epic += 1
        print("\033[95;1mЭпик\033[m")
    elif shans < 0.05:
        legendary += 1
        print("\033[33;1mЛегендарный\033[m")
    else:
        print("Ничего")
        _ = 0
    while _ < 20:
            _ += 1   
print("\033[31;1mОткрывает ПК\033[m")
for _ in range(0, 21):
    
    pcshans = random.random() 
    
    if pcshans > 0.20 and pcshans <= 0.70:
        pccommon += 1
        print("\033[32;1mОбычный\033[m")
    elif pcshans <= 0.20 and pcshans > 0.10:
        pcrare += 1
        print("\033[94;1mРедкий\033[m")
    elif pcshans <= 0.10 and pcshans > 0.05:
        pcepic += 1
        print("\033[95;1mЭпик\033[m")
    elif pcshans < 0.05:
        pclegendary += 1
        print("\033[33;1mЛегендарный\033[m")
    else:
        print("Ничего")
        _ = 0
        while _ < 20:
            _ += 1     

print(f"Вам выпало {common} обычных, {rare} редких, {epic} эпических, {legendary} легендарных")
bonus = 0
bonus1 = 0
if epic >= 3 and legendary <= 1:
    bonus += 5
    print("\033[36;1mУдача!\033[m")   
elif legendary > 1:
    bonus1 += 10
    print("\033[31;1mБольшая удача!\033[m")
    

pcbonus = 0
pcbonus1 = 0
print(f"Компьютеру выпало {pccommon} обычных, {pcrare} редких, {pcepic} эпических, {pclegendary} легендарных")
if pcepic >= 3 and pclegendary <= 1:
    pcbonus += 5
    print("\033[36;1mУдача!\033[m")   
elif pclegendary > 1:
    pcbonus1 += 10
    print("\033[31;1mБольшая удача!\033[m")
    

ochki = (common * 1) + (rare * 2) + (epic * 3) + (legendary * 4) + (bonus) + (bonus1)
pcochki = (pccommon * 1) + (pcrare * 2) + (pcepic * 3) + (pclegendary * 4) + (pcbonus) + (pcbonus1)
print("Ваши очки", ochki)
print("Очки ПК", pcochki)
if ochki > pcochki:
    print("Вы выйграли")
elif ochki < pcochki:
    print("Вы проиграли")
else: 
    print('Ничья')
