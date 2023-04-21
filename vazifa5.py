#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:54:52 2023

@author: rasuljon
"""

""" bro={'ism':'abdulaziz','yil':'2001','yosh':'22'}
bro_2={'ism':'samer','yil':'2005','yosh':'18'}
sis = {'ism':'vasila','yil':'2013','yosh':'10'}
print(bro)
print(bro_2)
print(sis)"""


"""cook = {'abdulaziz':'osh','samer':'shashlik','vasila':'somsa'}
print(f"Samerning sevimli taomi {cook['samer'].title()} ")
print(f"Vasilaning sevimli taomi {cook['vasila'].title()}")


phython ={'string':'matn','intger':'butun son','float':'o\'nlik son','print':'chqarish','appent':'qushish','del':'uchirish',}
for key,value  in sorted(phython.items()):
    print(f"{key.title()}  - {value} ")
    





dic = {'hello':'salom','labtop':'kompyutir','apple':'olma','car':'moshina'}
k = input("Kalit suzni kiriting...")
if k in dic :
    print({dic[k]})
elif k not in dic:
    print("Kechirasiz bunday kalit suz yuq ")"""
    
    
"""davlatlar ={'uzbekiston':'toshkent',"qirg'ziston":'beshkek','qozog\'iston':'astan','misr':'qoxira'}
print("Dunyo davlatlari")
for key,value in sorted(davlatlar.items()):    
    print(f"{key.upper()}")


print("Poytaxtlar")
for key,value in sorted(davlatlar.items()):
    print(f"{value.title()}")
    
con =input("Qaysi davlatni poytaxtini bilishni istaysiz...?")
cap =davlatlar.get(con)

if cap==None:
    print("kechirasiz bizda bu davlat haqida malumot yuq")
    
else:
    print(f"{con.upper()} ning poytaxti {cap.title()} shaxri")"""
    
    
    
    
"""ovqatlar ={'osh':'10','somsa':'8','shurva':'15','barak':'7','shashlik':'20','manti':'22'}
print('3-ta taom buyurtma bering ')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}- taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in ovqatlar:
        print(f"{buyurtma.title()}  {ovqatlar[buyurtma]}  junayh")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yuq")"""
        
magazin = {'gusht':'70000','non':'3000',
          'piyoz':'5000','kartoshka':'6000','makaron':'7000','pamedor':'20000','bodring':'10000'}
print("5 - mahsulot kiriting")
buyurtmalar = []
for n in range(5):
    buyurtmalar.append(input(f"{n+1} - mahsulot: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in magazin:
        print(f"{buyurtma.title()} {magazin[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q ")
        
     
    

    
    
    
    
    
    
        