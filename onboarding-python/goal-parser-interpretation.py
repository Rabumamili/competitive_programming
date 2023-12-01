class Solution(object):
    def interpret(self, command):
        strng =""
        for i in range (len(command)):
            if command[i]== "G":
                strng= strng + "G"
            elif command[i]=="(" and command[i+1]==")":
                 strng= strng + "o"
            elif command[i]=="("and command[i+1]=="a" and command[i+2]=="l" and command[i+3]==")":
                strng= strng +  "al"
        return strng
        
        
        