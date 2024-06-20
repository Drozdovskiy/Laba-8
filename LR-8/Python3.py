money = int(input("Ваша начальная сумма: "))
procent = float(input("Процентная ставка банка: "))
years = int(input("На сколько лет кладете?: "))

def money_(money, procent, years):
    i = 0
    while i < years:
        drop = (money/100) * procent
        money = money + drop
        i += 1
    print(f"Через {years} лет, ваша инвестиция вырастет до: {round(money, 2)}")

money_(money, procent, years)