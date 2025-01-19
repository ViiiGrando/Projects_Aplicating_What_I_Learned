#!/bin/python3

import math
import os
import random
import re
import sys

   
       

def verify_number():
    try:
     n = int(input('Input a number').strip())
    except ValueError:
     input('You typed a wrong value, please input any key to return  ')
     os.system('cls')#windows
     main()
    
    par = n % 2 == 0
    impar =  n % 2 == 1
    list1 = range(2,5)
    list2 = range(6,19)
    list3 = range (20,100)
    if  par and list1:
       print('Not Weird')
    elif par and list2:
       print('Not Weird')
    elif par and list3:
       print('Not Weird')
    elif impar and list1:
       print('Weird')
    elif impar and list2:
       print('Weird')
    elif impar and list3:
       print('Weird')
  


def main():
    verify_number()
    
if __name__ == '__main__':
    main()
    
    