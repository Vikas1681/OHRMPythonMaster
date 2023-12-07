import os
from configparser import ConfigParser
from getpass import getpass
class ConfigReader:
    
    def abcd(self):
        print(os.getcwd());
        print(os.path.dirname(os.path.abspath(__name__)))
        self.objConfig=ConfigParser()
        print(os.getlogin())
        self.objConfig.read("C://Users//u723399//Documents//NewSeleniumPythonMaster//Configuration//config.ini")
        print(self.objConfig.get("ENV_Details","URL"))
#         self.configFilePath = configFilePath
    

obj = ConfigReader()
obj.abcd()
    
