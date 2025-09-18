from datetime import datetime, date

def calculate_age(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, '%d.%m.%Y')
    except ValueError:
        return "Некоректний формат дати. Використовуйте формат ДД.ММ.РРРР."

    now = datetime.now()

    if birth_date > now:
        return "Дата народження не може бути в майбутньому."
    
    years = now.year - birth_date.year
    months = now.month - birth_date.month
    days = now.day - birth_date.day
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    if days < 0:
        months -= 1
        last_month_day = (now.replace(day=1) - datetime.timedelta(days=1)).day
        days += last_month_day

    if months < 0:
        years -= 1
        months += 12

    return (f"Вам {years} р. {months} міс. {days} дн. "
            f"{hours} год. {minutes} хв. {seconds} сек.")

def calculate_total_time(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, '%d.%m.%Y')
    except ValueError:
        return "Некоректний формат дати. Використовуйте формат ДД.ММ.РРРР."

    now = datetime.now()

    if birth_date > now:
        return "Дата народження не може бути в майбутньому."
    
    total_duration = now - birth_date
    
    total_seconds = (int)(total_duration.total_seconds())
    total_minutes = int(total_seconds // 60)
    total_hours = int(total_seconds // 3600)
    total_days = total_duration.days
    total_years = total_days // 365
    total_months = (total_days % 365) // 30

    return (f"Ви прожили: \n"
            f"  • Загалом: {total_years} р.\n"
            f"  • Або: {total_months} міс.\n"
            f"  • Або: {total_days} дн.\n"
            f"  • Або: {total_hours} год.\n"
            f"  • Або: {total_minutes} хв.\n"
            f"  • Або: {total_seconds} с.")

def show_calculator_menu():
    while True:
        print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃          Оберіть тип розрахунку             ┃")
        print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
        print("┃ 1. Розрахувати вік                          ┃")
        print("┃ 2. Розрахувати загальну тривалість          ┃")
        print("┃ 3. Назад                                    ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        choice = input("\nВиберіть пункт меню (1-3): ")

        if choice == '1':
            user_input = input("Введіть дату народження у форматі ДД.ММ.РРРР: ")
            age_info = calculate_age(user_input)
            print( "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(f"┃ {age_info}")
            print( "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print("\n           ↓↓↓↓↓↓           \n")
        elif choice == '2':
            user_input = input("Введіть дату народження у форматі ДД.ММ.РРРР: ")
            total_time_info = calculate_total_time(user_input)
            print( "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(f"┃ {total_time_info}")
            print( "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print("\n           ↓↓↓↓↓↓           \n")
        elif choice == '3':
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃ Повернення до головного меню... ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print("\n           ↓↓↓↓↓↓           \n")
            break
        else:
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃ Некоректний вибір. Будь ласка, виберіть 1, 2 або 3. ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print("\n           ↓↓↓↓↓↓           \n")

def show_main_menu():
    while True:
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃       Калькулятор віку       ┃")
        print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
        print("┃ 1. Перейти до калькулятора   ┃")
        print("┃ 2. Інформація про формули    ┃")
        print("┃ 3. Інформація про автора     ┃")
        print("┃ 4. Вихід                     ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        choice = input("\nВиберіть пункт меню(1-4): ")

        if choice == '1':
            print("\n           ↓↓↓↓↓↓           \n")
            show_calculator_menu()
        elif choice == '2':
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃                      Інформація про розрахунки                          ┃")
            print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
            print("┃ Розрахунок віку: виводить роки, місяці та дні, що минули, а також       ┃")
            print("┃ поточні години, хвилини та секунди.                                     ┃")
            print("┃ Розрахунок загальної тривалості: виводить загальну кількість років,     ┃")
            print("┃ місяців, днів, годин, хвилин та секунд, які були прожиті.               ┃")
            print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
            print("┃ Розрахунок віку:                                                        ┃")
            print("┃ - Роки: (поточний рік) - (рік народження).                              ┃")
            print("┃ - Місяці: (поточний місяць) - (місяць народження).                      ┃")
            print("┃ - Дні: (поточний день) - (день народження).                             ┃")
            print("┃ (Після розрахунку проводиться корекція, якщо кількість місяців          ┃")
            print("┃  або днів виявилася від'ємною).                                         ┃")
            print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
            print("┃ Розрахунок загальної тривалості:                                        ┃")
            print("┃ - Спочатку обчислюється загальний час між датами у секундах.            ┃")
            print("┃ - Далі ці секунди конвертуються у хвилини, години, дні, місяці та       ┃")
            print("┃  роки за допомогою ділення.                                             ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print("\n           ↓↓↓↓↓↓           \n")
        elif choice == '3':
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃ Автор: Артем Проценко ПД-22       ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print("\n           ↓↓↓↓↓↓           \n")
        elif choice == '4':
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃        Дякую за використання!     ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            break
        else:
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃ Некоректний вибір. Будь ласка, виберіть 1, 2 або 3. ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print("\n           ↓↓↓↓↓↓           \n")

if __name__ == "__main__":
    show_main_menu()