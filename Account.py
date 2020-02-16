import os

def login(user, password):
    os.system("taskkill.exe /F /IM steam.exe")
    os.chdir("C:\Program Files (x86)\Steam")
    os.system("start steam.exe -login {} {}".format(user, password))

def register(user,password):

    path = "config/users/{}.ini".format(user)
    f = open( path , "w")
    f.write(user)
    f.write("\n")
    f.write(password)
    f.close

def getpass(user):

    path = "config/users/{}.ini".format(user)
    f = open( path , "r")
    f.readline()
    password = f.readline()
    f.close
    return str(password)
    