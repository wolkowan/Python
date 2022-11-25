import delete
import edit
import view
import write


def start():
    print("Выберите действие")
    print("1. Новая запись\n2. Просмотр\n3. Изменение данных\n4. Удаление\n5. Выход")
    n=int(input())
    if n==1:

        write.New_Entry()
    elif n==2:
        view.print_all_to_console()
    elif n==3:
        pass
    elif n==4:
        delete.delete_str()
    if n==5:
        print("exit")

start()