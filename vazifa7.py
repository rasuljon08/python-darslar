#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:36:27 2023

@author: rasuljon
"""


# buyurtmalar = []
# print("Kerakli mahsulotlar ruyxatini kiriting")
# n =1
# while True:
#     savol=f"{n}-mahsulotni kiriting: "
#     buyurtma=input(savol)
#     buyurtmalar.append(buyurtma)
#     javob=input("Yana mahulot qushasizmi ? (ha/yo'q) : ")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
        
# print(f"{buyurtmalar}\n")      
        
        
print("Mahsulotlar va narxlarni kiritamiz.")
bozor={}
n=1
ishora=True
while ishora :
    mahsulot= input("Mahsulot nomini kiriting: ")
    narx = input(f"{mahsulot.title()}ning - narxini kiriting: ")
    bozor[mahsulot]=float(narx)
    
    javob=input("Yana mahulot qushasizmi ? (ha/yo'q) : ")
    if javob == "yo'q":
        ishora = False
    
  
buyurtmalar = []
print("Kerakli mahsulotlar ruyxatini kiriting")
n =1
while True:
    savol=f"{n}-mahsulotni kiriting: "
    buyurtma=input(savol)
    buyurtmalar.append(buyurtma)
    javob=input("Yana mahulot qushasizmi ? (ha/yo'q) : ")
    if javob == 'ha':
        n+=1
        continue
    else:
        break
        
for buyurtma in bozor:
    print(f"{buyurtma.title()} ning narxi {bozor[mahsulot]} sum")

if buyurtma not in bozor:
    print("Kechirasiz bizda {buyurtma.title()} yo'q")




