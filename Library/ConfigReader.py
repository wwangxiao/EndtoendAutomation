import configparser

def readConfigData(section,key):
    config=configparser.ConfigParser()
    # path="C:\\Users\\meifute\\PycharmProjects\\EndtoendAutomation\\ConfigurationFiles\\config.cfg"
    # config.read(path)
    config.read("../ConfigurationFiles/config.cfg")
    return config.get(section,key)

def readElementData(section,key):
    config=configparser.ConfigParser()
    config.read("../ConfigurationFiles/Elements.cfg")
    return config.get(section,key)

