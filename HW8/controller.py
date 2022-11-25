import view
import model


def start():

    while True:
        operator = view.startMenu()

        match operator:

            case "1":
                model.create_base()
                model.first_add()
            case '2':
                model.add()
            case '3':
                view.printAll()
            case '5':

                choice = view.view_info()
                if choice == '4':
                    view.print_row(model.find_status())

                elif choice == '3':
                    view.print_row(model.find_town())
                else:
                    print("Такого пункта нет в меню")

                # model.del_row()
            case '4':

                choice = view.view_info()
                if choice == '1':
                    view.print_row(model.find_by_id())

                elif choice == '2':
                    view.print_row(model.find_by_last_name())
                else:
                    print("Такого пункта нет в меню")


            case '6':

                choice = view.view_info()
                if choice == '1':
                   pass

                elif choice == '2':
                    pass


                else:
                    print("Такого пункта нет в меню")




            case '8':
                print("Выход")
                break
            case _ :
                print("Введено некорректное значение")





start()
