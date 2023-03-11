# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
count_ticket = int(input("введите количество билетов: "))

age_participant = []

for i in range(0, count_ticket):
    input_value = int(input(f"Введите возраст участника №{i + 1}:\n"))
    age_participant.append(input_value)


    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

    full_prise = sum(map(prise, age_participant))

    discount_prise = int(full_prise * 0.9)
    if count_ticket > 3:
        print("Стоимость билетов со скидкой: ", discount_prise)
    else:
        print("Общая стоимость билетов: ", full_prise)

        age = int(input('введите возраст'))

        if age < 18:
            print('Посещение конференции для Вас бесплатно')
        elif age >= 18 or age <= 25:
            print('Стоимость билета 990 рублей')
        elif age >= 26:
            print('Стоимость билета 1390 рублей')