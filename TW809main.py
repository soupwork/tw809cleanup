#
#python 3 scripting proposal
#Cisco 809 Local Logfile and StatsFile cleanup
#	I'd like to write a script to run on a server inside the SCADA Network
#	My script will need some libraries installed:
#		Netmiko
#		argparse
#		datetime
#		I might need getpass
#	
#	Input will be either an ip address at command line, 
#		a csv of IP addresses, or JSON file
#	Username/Password could be prompted/input using getpass for testing
#		Username/password could be a service account in the future
#	Script will ssh into a router using Netmiko
#	Script will get the hostname from Netmiko. 
#	Script will check uptime and 
#		check to see if four .txt files have been created by autorecovery script
#	Script will check the License Version on the 809
#	Script will copy from flash to SCP server the four files
#		Script will change destination filename to 
#			prepend the site hostname and append the date/time
#		Script will check the file size of coppied file with the file size on
#			the router. If they are the same, the Script will delete the files
#			off the router
#	Script will clear the counters
#	I am not sure how yet, but the Script will notify (Network team?) when a 
#		router has been up for less than 3 days

import argparse
import getpass
import datetime
import netmiko

from TW809model import NetObjGroup, IR809obj
from TW809view import UserPrompts
from NetmikoController import RemoteRouter

class CLIparams:
    def __init__(self):
        inputargs = argparse.ArgumentParser()
 
        inputargs.add_argument('-f', action='store',
            help='This option allowers user to specify a csv file - a list of IP Addresses')
        
        inputargs.add_argument('-ip',action='append',
            help='use this option to specify one or more ip addresses to change')

        cliargs = inputargs.parse_args()
        self.filename = cliargs.f
        self.ip = cliargs.ip
        
        #testing
        #self.filename = "testdata728.csv"
		

       
    def setTestOptions(self, params=""):
        """this is manually setting options that ought to be passed in from the command line.
        It will probably be removed later.
        This is called from Main, after options have been set in CLIparams Init"""
        #self.filename="test.csv"
        #self.ip = ['192.168.20.1','192.168.20.1','192.168.20.1']
        self.ip = ['192.168.20.1']
		
		


def main():
    print("inside main fn")

	#netObjDict=clearNetObjDict()
    options = CLIparams()
    #************************
    options.setTestOptions()
    loginID = ('djs','doug.sheehan')
    #*************************
    # 	
    view = UserPrompts()
    netobjgrp = NetObjGroup(options.ip, options.filename)
    objcount = netobjgrp.objcount
    print(objcount," IR809 objects created")			
    
    for index in range(objcount):
        tempdevDict = netobjgrp.share809dict(index)
        print("testing obj ", index, " ", tempdevDict['IPADDY'])
        #loginID=view.getLoginID()
        print("username is ", loginID[0])
        print("word is ", loginID[1])
        target=RemoteRouter(loginID,devDict=tempdevDict)
        #netobjgrp.update809dict(index,tempdevDict)
        filelist=['TW809-remove_prev_script.txt']
        #
        cmdlist = netobjgrp.prepareUpdateScripts(filelist)
        target.sendScript(ipAddy='192.168.20.1',cmdlist=cmdlist)

        cmdlist = netobjgrp.prepareUpdateScripts(['TW809-setIPSLA_script.txt'])
        target.sendScript(ipAddy='192.168.20.1',cmdlist=cmdlist)

    #end main

if __name__ == "__main__":
    print("startiing from __main__")
    main()  


     #   testcontroller=controller.RemoteRouter(loginID,options.tr)
     #   hostname = testcontroller.getHostname(options.tr)
  
        #print("plaintext is ",checkpw) #this only applies for -p7


        #end main program