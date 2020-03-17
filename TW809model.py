#This is my Model. This is the Data. These are the methods that act directly on the data.
#
import datetime
import os.path


class IR809obj:
    """this is a cisco IR809 object. It will have a dictionary to store its parameters"""
    
    def __init__ (self, ip=''):
        self.ip=ip
        
        self.devDict = {'IPADDY':ip, 'HOSTNAME':'','SHVER':'','DIRFLASH':'','SHIPINTBRI':'',
            'SHCELL':'','UPTIME':'','VERSION':'','MODELNUM':'','SERIALNUM':'','CONFREG':''}
       

    def printip(self):
        """this is just to test my IR809 object"""
        print("object ip is ", self.ip)


class NetObjGroup:
    """this is a group of IR809 objects"""

    def __init__ (self, ip='', filename=''):
        self.ip=ip
        self.filename = filename
        self.netobjlist = [] #this is a list containing network objects
        iplist = []

        if filename and not ip:
            try :
                with open(filename, 'r') as infile:
                    iplist=infile.readlines()
                    print(iplist)

            except:
                print("unable to open file")
        elif ip and not filename:
            iplist = ip

        elif  ip and filename:
            #call the view!
            #filename may be a script file to pass for all the ip's
            print("ip and filename both")

        elif  ip and not filename:
            #call the view!
            print("neither IP nor filename")

        else: 
            print("error condition. how did i miss a state?") 

        
        index=0
        for element in iplist:
            ip = element.strip()
            
            tempobj = IR809obj(ip)
            self.netobjlist.append(tempobj)


           # self.netobjlist
            index +=1
            if index > 500:
                print('index is going to exceed 500')
                break
        
        print("testing from model - netobjlist[0]", self.netobjlist[0].devDict['IPADDY']) 
        self.objcount = index    

    def share809dict (self, index):
        tempDict=''
        if index <= self.objcount:
            tempDict = self.netobjlist[index].devDict

        return(tempDict)  

    def update809dict(self, index, tempDict):
        temp809dict = self.netobjlist[index]
        for key in tempDict:
            #temp809dict[key] = tempDict[key]
            print("temp dictionary key is ", key, "  ",tempDict[key])
            print("existing dictionary key is ", key, "  ",temp809dict[key])

    def prepareUpdateScripts(self, filelist):
        cmdlist=[]
        for filename in filelist:
            with open(filename, 'r') as scriptfile:
                cmd = scriptfile.readlines()
                # cmd = str(nextcmd)
                # cmd = cmd.strip()
                # cmdlist.append(cmd)
        print("cmdlist ", cmd)
        return(cmd)        

if __name__ == "__main__":
    print("startiing from model>>__main__")
    print("working dir is ", os.getcwd())
    #testNetObjGroup = NetObjGroup(filename='testips.csv') 
    #testNetObjGroup = NetObjGroup(ip=['192.168.20.1'])
    testNetObjGroup = NetObjGroup(ip=['192.168.20.1','192.168.20.2','192.168.20.3'])