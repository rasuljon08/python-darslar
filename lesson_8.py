#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:42:11 2023

@author: rasuljon
"""


unli =['i',' e', 'a', 'o','u'," oʻ"]
undosh =['b','v','g','d','j','d','y','k','l','m','n','ng','p','r','s','t','f','x','s','ch','sh','q'," gʻ",'h']
xarf =input("Biron harf kiriting sizga unli yoki undosh harf ekanligini aniqlab beramiz:  " )
if xarf in unli:
    print(f"{xarf} bu unli harf")
elif xarf in undosh:
    print(f"{xarf} bu undosh harf")

else:
    print("o'zbek tilida bunaqa xarf yuq ")
