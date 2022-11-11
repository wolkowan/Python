import user_interface


def create():
    style = 'style="font-size:22px;"'

    html = '<html>\n <head></head>\n <body>\n'
    html +=' <p {}> Temperature: {} c</p>\n'\
        .format(style, user_interface.temp_viev)
    html +=' <p{}> Wind_speed: {} ms</p>\n'\
        .format(style, user_interface.wind_viev)
    html +=' <p{}> Pressure: {} mmHg</p>\n'\
        .format(style, user_interface.press_viev)
    html +=' <body>\n</html> '

    with open('index.html', 'w') as page:
        page.write(html)
    return html