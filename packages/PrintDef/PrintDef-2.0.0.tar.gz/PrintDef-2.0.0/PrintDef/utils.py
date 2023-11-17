

def HelloWorld():
    print("\nHello, world!\n" *2)

def PrintHelp():
    print(f"print(value, ..., sep='', end='\н(n)', file=sys.stdout, flush=False)")

def greet():
    name = input("Введите ваше имя: ")
    print("Hello,", name + "!")

def game():

    while True:
        print('\n1.Игра 1 \n2.Игра 2 \n3.Игра 3\n')
        select = input("Выберите цифру для отображение названия игры: ")
        
        if select == "1":
            print("Игра под номером 1 - называется - Valorant\n")
        elif select == "2":
            print("Игра под номером 2 - называется - Owerwatch 2\n")
        elif select == "3":
            print("Игра под номером 3 - называется - Paladins\n")
        else: print("Нет такой цифры\n")
