'''
Created on 12-Feb-2019

@author: sairam
'''
import sys
from getpass import _raw_input


if __name__ == '__main__':
    pass

try:
    
    f = open("./test12.txt", mode = "r",encoding = 'utf-8')

    print(f.read())
    
finally:
    f.close()

#f.write("write dummy")


_raw_input("press any key")
