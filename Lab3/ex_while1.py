"""
Name: prapatsorn tempiam
ID: 364411760009
Grop: MIT421
"""

# while loop

# รับค่าจากผู้ใช้ไปเรื่อยๆ แต่หากผู้ใช้ใส่ค่าเลข 0 ให้หยุดการทำงานของลุป
i = 0
while i < 10:
    num = int(input("Enter an integer: "))
    print("your number is : ",num)
    if num ==0:
        print("good bye.")
        continue # continue
    i += 1

