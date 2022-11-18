import view
import model






def start():


    operators = view.startMenu()
    if operators==1:
        result= view.inputNote()
        return result
    elif operators==2:

        fileFormat = view.AskFormatForPrintFile()
        if fileFormat == 1:
            result= view.printAllCSV()

        if fileFormat == 2:
            result= view.printAllMd()
        if fileFormat == 3:
            result= view.printAllHtml()
        if fileFormat == 4:
            result= view.printAllTxt()

        return result
    elif operators==3:
        print("Выберете формат файла для загрузки базы данных из внешнего источника.\n1. csv;\n2. md;\n3. html;\n4. txt")
        fileFormat= int(input())
        if fileFormat==1:
            # model.importDataCSV()
            print("в разработке")
        if fileFormat==2:
            print("в разработке")
        if fileFormat==3:
            print("в разработке")
        if fileFormat==4:
            print("в разработке")

    elif operators==4:
        print("Выход")






