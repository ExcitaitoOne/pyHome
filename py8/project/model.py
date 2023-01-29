import controller
import csv
import json
#f = open("base.txt", "r", encoding="utf-8")
def readFile():
    with open("base.txt", "r", encoding="utf-8") as f:
        list1 = f.readlines()
    return list1

list1 = readFile()

def serch(): #Поиск 1 пункт меню
    with open("base.txt","r+", encoding="utf-8") as f:
        x = input()
        list1 = f.readlines()
        for i in range(len(list1)):
            FINDER = list1[i].find(x)
            if FINDER > -1:
                return list1[i]

def serch_post(): # 2 пункт меню
    with open("base.txt","r+", encoding="utf-8") as f:
        x = input()
        list1 = f.readlines()
        for i in range(len(list1)):
            a = list1[i].split()
            FINDER = a[2].find(x)
            if FINDER > -1:
                print(list1[i])
            continue

def serch_salary(): #3 пункт меню
    with open("base.txt","r+", encoding="utf-8") as f:
        x = input()
        list1 = f.readlines()
        for i in range(len(list1)):
            a = list1[i].split()
            FINDER = a[3].find(x)
            print(FINDER)
            if FINDER > -1:
                print(list1[i])
            continue

def deleter(list1):
    x = input()
    for i in range(len(list1)):
        FINDER = list1[i].find(x)
        if FINDER > -1:
            del list1[i]
            break
    with open(r"base.txt", "w") as f:
        f.writelines(list1)

def _Save(list1): # сохранение в новый файл тхт
    with open("base.txt", "w") as f:
        for i in list1:
            f.writelines(list1 + '\n')


#9 пункт меню
def quit_menu():
    print(f"Вы точно хотите выйти?\n да/нет")
    x = input()
    if x == "да":
        print("Завершение работы.")
    elif x == "нет":
        controller.start()
    else:
        [print("Выберите из предложенного\n да/нет")]
        quit_menu()

def _SaveCSV(): # сохранение в новый файл Csv
    with open('base.csv', 'w', newline='') as csvF:
        writer = csv.writer(csvF, delimiter=",")
        with open("base.txt") as f:
            href = f.readlines()
            writer.writerow([href])

def _SaveJSON():
    with open("data_file.json", "w") as write_file:
        json.dump(list1, write_file)

def _add():
    with open("base.txt", "a+", encoding="utf-8") as f:
        f.writelines(input()+"\n")

def fileUpdate():
    x = serch()
    x1 = list(x.split())
    print("Введите номер элемента")
    d = int(input())
    print("Ведите изменяемое")
    s = input()
    x1[d] = s
    x1 = ",".join(x1)
    list1.append(x1)
    print(list1)
    for i in range(len(list1)):
        FINDER = list1[i].find(x)
        if FINDER > -1:
            del list1[i]
            break
    with open(r"base.txt", "w") as f:
        f.writelines(list1)

