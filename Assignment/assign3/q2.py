"""
Name: prapatsorn tempiam
ID: 364411760009
Grop: MIT421
"""

# 2.เขียนฟังก์ชันเพื่อยกกำลังสองสมาชิกทุกตัวใน list และ return list ที่เป็นผลลัพธ์จากการยกกำลังสองออกมา
# #กำหนดให้ฟังก์ชันนี้รับ paramrter 1 คือ listA ที่มีสมาชิกเป็นจำนวนใดๆ

a = int(input("key1:"))
b = int(input("key2:"))
c = int(input("key3:"))

l = [a,b,c]
power = 2

for i in range(len(l)):
    print(l[i],"ยกกำลัง",power,"เท่ากับ",pow(l[i], power))


