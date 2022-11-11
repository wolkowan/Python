import data_provider
import logger
def temp_viev():
    data= data_provider.get_temp()
    logger.temp_logger(data)
    return data
def press_viev():
    data= data_provider.get_press()
    logger.press_logger(data)
    return data
def wind_viev():
    data= data_provider.get_wind()
    logger.wind_logger()
    return data


