#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:36:06 2023

@author: rasuljon
"""

# from random import randint

# a = randint(1, 500)
# b = randint(1, 500)
# c =  int(input("{} + {} = ".format(a, b)))

# if c ==(a+b):
#     print("To'gri javob")
# else:
#     print("Xato javob")



yil = int(input("Biron yilni kiriting:  "))
if yil % 4 ==0 and yil %100!=0:
    print("Kabisa yil")
elif yil % 400==0:
    print("kabisa yil")
else:
    print("Kabisa yili emas")
