#
#This is the CLI view. no GUI elements.
import getpass
import datetime
import os.path


class UserPrompts:
    def __init__(self):
         print("init UserPrompts")

    def getLoginID(self):
        self.username = input("enter the username to authenticate to router/switch: ")
        self.pword=getpass.getpass("please enter password <hidden> :")
        print ("username is :", self.username)
        
        return(self.username,self.pword)