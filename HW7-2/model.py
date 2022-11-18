
def newNoteCSV(name, surname, number):
    with open('phonebook.csv', 'a', encoding="utf-8") as file:
        file.write("{},{},{} \n".format(name, surname, number))

def newNoteMD(name, surname, number):
    with open('phonebook.md', 'a', encoding="utf-8") as file:
        file.write("{}\n{}\n{} \n\n".format(name, surname, number))

def newNoteTXT(name, surname, number):
    with open('phonebook.txt', 'a', encoding="utf-8") as file:
        file.write("{} {}: phone number is  {} \n".format(name, surname, number))




def newNoteHTML(name, surname, number):

    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Name is: {} </p>\n' \
        .format(style, name)
    html += '    <p {}>Surename is: {} </p>\n' \
        .format(style, surname)
    html += '    <p {}>Number is: {}</p>\n' \
        .format(style, number)
    html += '  </body>\n</html>'

    with open('phonebook..html', 'a', encoding="utf-8") as page:
        page.write(html)


