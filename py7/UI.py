import Model as m
def import_p():
    print("Введите телефон, имя")
    m._addTele()
def export_p_txt():
    print("Запись в файл..")
    m._SaveTXT()
def readFile():
    m._readFile_s()

def export_p_CSV():
    print("Запись в файл..")
    m._SaveCSV()

def menu():
    print("выберете из пункта меню \n"
          "1. Внесение данных \n"
          "2. Запись даных в текстовый файл \n"
          "3. Чтение файла\n"
          "4. Запись данных в CSV")
    x = int(input())
    if x == 1:
       import_p()
    elif x == 2:
       export_p_txt()
    elif x == 3:
       readFile()
    elif x == 4:
       export_p_CSV()
    else:
        print("Неверно введены даные")

