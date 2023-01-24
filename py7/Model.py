import csv
def _readFile():
    with open("Base.txt") as f:
        list1 = f.readlines()
    return list1

def _readFile_s():
    with open("Base.txt") as f:
        list1 = f.readlines()
        print(*list1)
def _SaveTXT(): # сохранение в новый файл тхт
    with open("Newbase.txt", "w") as f:
        f.writelines(_readFile())
        list1 = f.writelines(" ")


def _addTele(): #добавление нового номера в справочник
    with open("Base.txt", "a+") as f:
        list1 = f.writelines(input()+"\n")

def _SaveCSV(): # сохранение в новый файл тхт
    file = open("Base.txt")
    with open('Newbase.csv', 'w', newline='') as csvF:
        writer = csv.writer(csvF, delimiter=";")
        with open("Base.txt") as f:
            href = f.readlines()
            writer.writerow([href])






