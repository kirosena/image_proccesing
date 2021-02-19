import odroid_wiringpi as wpi
import time
import re
import sys


class Serial:
    def __init__(self):
        self.con = wpi.serialOpen('/dev/ttySAC0', 57600)
        if not self.con:
            print("No Connection")
            sys.exit(0)
        self.q = 0
        self.g1=self.g2=self.g3=self.g4=0
        self.data = ''
        self.recv = ''


    def readAll(self):
        try:
            while wpi.serialDataAvail(self.con):
                self.recv += chr(wpi.serialGetchar(self.con))
            # print(self.recv)
            if len(self.recv) > 0:
                return (self.recv)
        except KeyboardInterrupt:
            print("System Exit")
            sys.exit(0)
        except:
            pass
    
    def read(self):
        try:
            while wpi.serialDataAvail(self.con):
                self.data += chr(wpi.serialGetchar(self.con))

            if self.data:
                # print(self.data)
                prs = re.compile(r'!(\S*)@(\S*)#(\S*)%(\S*)')
                dataParsing = re.search(prs, str(data))
                if dataParsing:
                    self.g1 = dataParsing.group(1)
                    self.g2 = dataParsing.group(2)
                    self.g3 = dataParsing.group(3)            
                    self.g4 = dataParsing.group(4)
           
            return self.g1,self.g2,self.g3,self.g4
        except KeyboardInterrupt:
            print("System Exit")
            sys.exit(0)
        except:
            pass
            return self.g1,self.g2,self.g3,self.g4


    def write(self, p1=0, p2=0, p3=0, p4=0, p5=0,p6=0,p7=0):
        try:
            # packet ='!'+str(p1)+'@'+str(p2)+'#'+str(p3)+'%'+str(p4)+'&'+str(p5)+"="+str(p6)+"_"+str(p7)+'\n'
            packet ='!'+str(p1)+'@'+str(p2)+'#'+str(p3)+'\n'
            wpi.serialPuts(self.con, packet)
            # print(packet)
        except KeyboardInterrupt:
            print("System Exit")
            sys.exit(0)
        except:
            print('error sending message')
            pass
    
    def write2(self, p1=0, p2=0, p3=0, p4=0, p5=0,p6=0,p7=0):
        try:
            # packet ='!'+str(p1)+'@'+str(p2)+'#'+str(p3)+'%'+str(p4)+'&'+str(p5)+"="+str(p6)+"_"+str(p7)+'\n'
            packet ='!'+str(p1)+'@'+str(p2)+'#'+str(p3)+'%'+str(p4)+'&'+str(p5)+'\n'
            wpi.serialPuts(self.con, packet)
            # print(packet)
        except KeyboardInterrupt:
            print("System Exit")
            sys.exit(0)
        except:
            print('error sending message')
            pass