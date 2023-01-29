import model
def show_menu():
    print("\n" + "=" * 50)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def menu_action(x):
    if x == 1:
        print("Введите имя сотрудника")
        print(model.serch())
    elif x == 2:
        print("Введите должность сотрудника")
        print(model.serch_post())
    elif x == 3:
        print("Введите зарплату сотрудника")
        print(model.serch_salary())
    elif x == 4:
        print("Ведите Имя, Должность, Зарполату")
        model._add()
    elif x == 5:
        print("Удалить сотрудника")
        print(model.deleter(model.list1))
        print(*model.list1)
    elif x == 6:
        model.fileUpdate()
    elif x == 7:
        model._SaveJSON()
    elif x == 8:
        model._SaveCSV()
    elif x == 9:
        model.quit_menu()
    else:
        print("Ошибка! Неверно введено значение")

