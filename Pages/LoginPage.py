
from Library import ConfigReader
class LoginClass:
    def __init__(self,obj):
        global  driver
        driver=obj

    def enter_name(self,username):
        inputs = driver.find_elements_by_class_name(ConfigReader.readElementData("Login", "username"))
        inputs[0].send_keys(username)

    def enter_passwd(self,passwd):
        inputs = driver.find_elements_by_class_name(ConfigReader.readElementData("Login", "passwd"))
        inputs[1].send_keys(passwd)
    def click_button(self):
        driver.find_element_by_class_name(ConfigReader.readElementData("Login", "button")).click()