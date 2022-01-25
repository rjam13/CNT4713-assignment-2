from re import S
import socket
from unittest import result


class Assignment2:
    def __init__(self, year: int):
        self.year = year #assuming this is birth year from tellAge

    def tellAge(self, currentYear: int): 
        print('Your age is ' + str(currentYear - self.year - 1)) 
        #-1 assumes that birthday for currentYear have not occured

    def listAnniversaries(self) -> list: #list of decade anniversaries from variable year to 2022
        return [x*10 for x in range(1, (2021 - self.year) // 10 + 1)]

    def modifyYear(self, n: int) -> str:
        return str(self.year // 100) * n + str(self.year * n)[0::2]

    @staticmethod
    def checkGoodString(string: str) -> bool:
        numOfDig = 0
        for x in string: 
            if x.isdigit():
                numOfDig += 1
        return len(string) >= 9 and string[0].isalpha() and numOfDig == 1

    @staticmethod
    def connectTcp(host: str, port: int) -> bool:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            sock.connect((host, port))
        except:
            return False
        finally:
            sock.close()
        return True

retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
