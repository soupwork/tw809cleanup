#
#This is the Controller. 
#it handles the SSH connections out to the devices.
#it uses Netmiko.
#should this be one or more classes, or just functions

import netmiko
import os

class RemoteRouter():
    """create a router object for Netmiko. """
    def __init__(self,loginID,ipAddy='', devDict=''):
        if ipAddy or devDict:
            self.ipAddy = ipAddy
            self.loginuser=loginID[0]
            self.loginpass=loginID[1]
            
        if devDict:
            print("found Dev Dictionary")
            self.ipAddy=devDict['IPADDY']    
            self.devDict = devDict
        else:    
            print("initialze blank dict in RemoteRouter init")
            self.devDict = {'IPADDY':ipAddy, 'HOSTNAME':'','SHVER':'','DIRFLASH':'','SHIPINTBRI':'',
            'SHCELL':'','UPTIME':'','VERSION':'','MODELNUM':'','SERIALNUM':'','CONFREG':''}

        routername = ""
        net_connect = self.connectToRouter(self.ipAddy)

        if net_connect == "no connect":
            print("no connection")
            
        else:    
            routername = self.getHostname(net_connect)
  
        
        if routername == "":
            print("unable to connect to remote router")
        else:    
            print("remoterouter is ", routername)
        
        self.devDict['HOSTNAME'] = routername
       
        

    def connectToRouter(self, ipAddy, fn=''):
        
        #
        cisco = {
            'device_type': 'cisco_ios',
            'host': ipAddy,
            'username': self.loginuser,
            'password': self.loginpass,
            }
        
        try:
            net_connect = netmiko.ConnectHandler (**cisco)
            self.devDict['SHIPINTBRI'] = net_connect.send_command('sh ip int brie')
            print( self.devDict['SHIPINTBRI'])
            self.devDict['SHVER'] = self.ShowVer(net_connect)
            print( self.devDict['SHVER'])
            print("end sh ver")
            privlevel = net_connect.send_command('show priv')
            self.devDict['DIRFLASH'] = self.getFilenames(net_connect)
            print("dir flash: is ")
            print( self.devDict['DIRFLASH'])

        except:
            print("unable to connect to host-connectToRouter")    
            return("no connect")

       
             
        return (net_connect)              
    #end connectToRouter

 
    def ShowVer(self,net_connect):
        getver=net_connect.send_command('sh version')
        print(getver)   

    def getHostname(self,net_connect):
        #
        privlevel = net_connect.send_command('show priv')
        print("priv level is ",privlevel)
        if privlevel=="Current privilege level is 15":
            hostname = net_connect.send_command('sh run | inc host')
            self.hostname = hostname[9:]
            print("hostname is ", self.hostname)
        else:
            print("insufficient Privilege Level")  
            self.hostname=''  
        return(self.hostname)

    def getFilenames(self, net_connect):
        dirflash = net_connect.send_command('dir flash:')
        
        return(dirflash)

    def sendScript(self,ipAddy, cmdlist, log=True):
        loglist = []
        print("inside sendScript")
        net_connect = self.connectToRouter(ipAddy)
        log = net_connect.send_config_set(cmdlist)
        print("log in sendscript is ", log)

   


if __name__ == "__main__":
    print ("controller is main")
    loginuser = ''
    loginpass = ''
    testloginID=(loginuser,loginpass)
    ipAddy="192.168.20.1"
    print("working dir is ", os.getcwd())
    router_ssh = RemoteRouter(testloginID, ipAddy)
   