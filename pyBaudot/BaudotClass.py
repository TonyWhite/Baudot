# -*- coding: UTF-8 -*-
import sys

# Author: Roshan Mehta


class baudotClass(object):
    mapString = [
    ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"],

    ["{NULL}", "E", "{LF}", "A", " ", "S", "I", "U", "{CR}", "D", "R", "J", "N", "F", "C", "K", "T", "Z", "L", "W", "H", "Y", "P", "Q", "O", "B", "G", "{FIGS}", "M", "X", "V", "{LTRS}"],

    ["{NULL}", "3", "{LF}", "-", " ", "'", "8", "7", "{CR}", "{ENQ}", "4", "{BELL}", ",", "!", ":", "(", "5", "+", ")", "2", "£", "6", "0", "1", "9", "?", "&", "{FIGS}", ".", "/", ";", "{LTRS}"]
]
    
    


    def __init__(self):
        self.error = False
    
    def baudotEncoder(self, msg):
        self.error = False
        orignalMsg = msg.upper()
        flagChar = True
        binaryMsg = ""
        
        
        if len(orignalMsg) > 0:
            i = 0
            while i < len(orignalMsg):
                
                if self.alphaCheck(orignalMsg[i]):
                    if not flagChar:
                        flagChar = True
                        binaryMsg = binaryMsg + self.mapString[0][31] + " "
                    binaryMsg = binaryMsg + self.getBinary(orignalMsg[i]) + " "
                elif self.specialCheck(orignalMsg[i]):
                    if flagChar:
                        flagChar = False
                        binaryMsg = binaryMsg + self.mapString[0][27] + " "
                    binaryMsg = binaryMsg + self.getBinary(orignalMsg[i]) + " "
                i += 1
        return binaryMsg
    
    def alphaCheck(self, oneChar): 
        flagChar = False             
        for i in xrange(1,31):
            if ((i != 2) or (i != 8) or (i != 27)):
                if oneChar == self.mapString[1][i]:
                    flagChar = True
                    break
        return flagChar
    
    def specialCheck(self, oneChar):
        flagChar = False             
        for i in xrange(1,31):
            if (i != 2) or (i != 8) or (i != 9) or (i != 11) or (i != 27):
                if oneChar == self.mapString[2][i]:
                    flagChar = True
                    break
        if oneChar == "\n":
            flagChar = True    
        return flagChar
    
    def getBinary(self, oneChar):
        binaryChar = ""
        for i in xrange(1,31):
            if oneChar == self.mapString[1][i].decode('utf-8') or oneChar == self.mapString[2][i].decode('utf-8'):          
                binaryChar = self.mapString[0][i];
                break;
        if oneChar == "\n":
            binaryChar = self.mapString[0][8] + " " + self.mapString[0][2]
        return binaryChar   
    
    def baudotDecoder(self, msg):
        self.error = False
        textMsg = ""
        i = 0
        if len(msg) > 4:
            if msg[0:5] == self.mapString[0][31] or msg[0:5] == self.mapString[0][27]:
                flagChar = True
                if msg[0:5] == self.mapString[0][31]:
                    flagChar = True
                else:
                    flagChar = False
                while i < len(msg):
                    oneBinary = msg[i:i+5]
                    resultChar = self.getText(oneBinary, flagChar)                    
                    if oneBinary == self.mapString[0][31]:
                        flagChar = True
                    elif oneBinary == self.mapString[0][27]:
                        flagChar = False
                    elif oneBinary == self.mapString[0][8]:
                        try:
                            if msg[i+6:i+11] == self.mapString[0][2]:
                                textMsg = textMsg + "\n"
                                i +=6
                            else:
                                sys.stderr.write("The LF character must ALWAYS follow a CR")
                        except Exception as e:
                            sys.stderr.write("Exception somewhere in Decoding :\n" + str(e))
                    else:
                        textMsg = textMsg + resultChar
                    i += 6
            else:
                self.error = True
                sys.stderr.write("The string must begin with LTRS (11111) or FIGS (11011)")
     
        return textMsg
    
    def getText(self, oneBinary, flagChar):
        resultChar = ""
        flagBinary = True
        for i in xrange(5):
            if (not oneBinary[i] == "0") and (not oneBinary[i] == "1"):
                flagBinary = False
        if len(oneBinary) == 5:
            for j in xrange(32):
                if self.mapString[0][j] == oneBinary:
                    if flagChar:
                        resultChar = self.mapString[1][j]
                        break
                    resultChar = self.mapString[2][j]
                    break
        else:
            self.error = True
        return resultChar
    
def converter():
    bauObject = baudotClass()
    while True:
        try:
            option = int(raw_input("1 for Encoding :: 2 for Decoding :: 3 for Exit\n"))
            if option == 1:
                x = raw_input("\nEnter a text string :").strip() 
                print "\nEncoded String : " + bauObject.baudotEncoder(x).strip()
            elif option == 2:
                x = raw_input("\nEnter an encoded string :").strip() 
                print "\nDecoded String : " + bauObject.baudotDecoder(x).strip()
            elif option == 3:
                exit()              
        except Exception as e:
            sys.stderr.write("\nInvalid Choice : " + str(e))
           
        
    
if __name__ == '__main__':
    converter()
        
    
        
                

                    
                                                    
                                                                    
                            
                                
                        
                    
                        
                    
                
                
                
            
         
        
        
        