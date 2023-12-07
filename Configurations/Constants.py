import os
import sys

class Constants:
    driver = "chrome"
    URL = "https://opensource-demo.orangehrmlive.com/"
    Username = "Admin"
    Password = "admin123"


### Waits
    DEFAULT_WAIT=15

    Project_Path = str(os.getcwd())[:str(os.getcwd()).find('Configurations')]
    sys.path.insert(0, Project_Path)


    



