# import view

def newNoteCSV(name, surname, number, info):
    with open('phonebook.csv', 'a', encoding="utf-8") as file:
        file.write("{},{},{},{} \n".format(name, surname, number, info))

def newNoteMD(name, surname, number, info):
    with open('phonebook.md', 'a', encoding="utf-8") as file:
        file.write("{}\n{}\n{}\n{} \n\n".format(name, surname, number, info))

def newNoteTXT(name, surname, number, info):
    with open('phonebook.txt', 'a', encoding="utf-8") as file:
        file.write("{} {}: phone number is  {}, comments: {} \n".format(name, surname, number, info))

def newNoteHTML(name, surname, number, info):

    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Name is: {} </p>\n' \
        .format(style, name)
    html += '    <p {}>Surename is: {} </p>\n' \
        .format(style, surname)
    html += '    <p {}>Number is: {}</p>\n' \
        .format(style, number)
    html += '    <p {}>Comments: {}</p>\n' \
        .format(style, info)
    html += '    <p>----------------------------</p>\n'

    html += '  </body>\n</html>'

    with open('phonebook.html', 'a', encoding="utf-8") as page:
        page.write(html)

# def importDataCSV():
#     path= view.inputPath()
#     file=open(path,'a')
#     cont=file.read()
#     with open('phonebook.txt', 'a', encoding="utf-8") as Homefile:
#         Homefile.write("{} \n".format(cont))
#     file.close()



