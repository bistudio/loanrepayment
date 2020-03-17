import datetime as dt
import random as rnd

# variables

try:
    userid = str(input("Please enter userid!"))
    login_name = str(input("Please enter login name"))
    pwd = str(input("Please enter your password!"))
except:
    raise ValueError("You have entered incorrect login details, please check and retry!")
