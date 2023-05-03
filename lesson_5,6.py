#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:16:01 2023

@author: rasuljon
"""


# a =input("Kiriting")
# print(a[::-1].capitalize())


# a=input("so`zlarni kiriting:")
# a=a.split()
# print(a[1],a[0])

# a = (input("Uch xonali son kiriting:  "))

# print(int(a[0])+int(a[1])+int(a[2]))


soat1 = int(input("1- soat:  "))
menut1 =int(input("1-menut:  "))
secund1 =int(input("1-secund:  "))

soat2 = int(input("2- soat:  "))
menut2 =int(input("2-menut:  "))
secund2 =int(input("2-secund:  "))


secund = (soat2-soat1)*3600+(menut2-menut1)*60+(secund2-secund1)
print("secund:  {}".format(secund))