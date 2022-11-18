# import data_generation as dg
import interface as ui
import logger as lg
import controller


# dg.start() # генерация базы контактов

controller.init_data_base('base_phone.csv')
ui.ls_menu()
