import os

def login(user, password):
    os.system("taskkill.exe /F /IM steam.exe")
    os.chdir("C:\Program Files (x86)\Steam")
    os.system("start steam.exe -login {} {}".format(user, password))