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



class CLIparams:
    def __init__(self):
        inputargs = argparse.ArgumentParser()
 
        inputargs.add_argument('-f', action='store',
            help='This option allowers user to specify a csv file - a list of IP Addresses')
        
        inputargs.add_argument('-ip',action='append',
            help='use this option to specify one or more ip addresses to change')

        cliargs = inputargs.parse_args()
        self.filename = cliargs.f
		self.ip = 
        #testing
        #self.filename = "testdata728.csv"
		 self.cliDict={'IPADDRESS':cliargs.ip, 'TESTROUTER':cliargs.tr, 'LOG':cliargs.log , \
             'LOGFILE':cliargs.logfile ,'VERBOSE': cliargs.verbose, 'CHANGE':cliargs.change,'VERIFIY':cliargs.verify, 'FILENAME':cliargs.f ,'GUI':cliargs.gui}

       
    def setTestOptions(self):
        """this is manually setting options that ought to be passed in from the command line.
            It will probably be removed later.
            This is called from Main, after options have been set in CLIparams Init"""
        #self.filename="test.csv"
        #self.cliDict['IPADDRESS']=['192.168.20.1']
        #self.cliDict['TESTROUTER']= '192.168.20.1'
		pass
		
	def evalIPListAndFilename(self):
        """this fn is to do a quick check on ip list and filename parms, The script needs either a file with IP's or one or more IP's passed in from the cli to run."""
        fileOrIP = True

        #no filename, no ip address,
        if not self.cliDict['FILENAME'] and not self.cliDict['IPADDRESS']:
            if self.cliDict['TESTROUTER']:
                self.cliDict['IPADDRESS'] = self.cliDict['TESTROUTER']
                model.objdict['IPADDRESS'] = self.cliDict['TESTROUTER']

            else: # No filename,no ip address, no test router
                self.fileOrIPorTR=False

        elif self.cliDict['FILENAME'] and not self.cliDict['IPADDRESS']:
            """load up to 500 ip addresses from filename"""
            linecount = model.loadMaxIPlist(self.cliDict['FILENAME'])
            self.cliDict['IPADDRESS'] = model.objdict['IPADDRESS']

        if not self.cliDict['TESTROUTER'] and self.cliDict['IPADDRESS']:  #no TestRotuter Defined
            self.cliDict['TESTROUTER'] =  self.cliDict['IPADDRESS'][0]
            print(self.cliDict['TESTROUTER'])
            	
		
		return(fileOrIP)

		
		
def main():
		print("inside main fn")
		#netObjDict=clearNetObjDict()

    options=CLIparams()
    #*************************
    #options.setTestOptions()
    #*************************	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
if __name__ == "__main__":
    print("startiing from __main__")
    main()  


     #   testcontroller=controller.RemoteRouter(loginID,options.tr)
     #   hostname = testcontroller.getHostname(options.tr)
  
        #print("plaintext is ",checkpw) #this only applies for -p7


        #end main program