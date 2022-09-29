"""
Name: prapatsorn tempiam
ID: 364411760009
Grop: MIT421
"""

"""
# Question 2
เขียนโปรแกรมรับอินพุต 1 ตัว ที่เป็นจำนวนจริง และตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่า 0, น้อยกว่า 0 หรือเท่ากับ 0
 - ถ้ามีค่ามากกว่า 0 ให้ตรวจสอบต่อว่าเป็นเลขคู่หรือเลขคี่
    - ถ้าเป็นเลขคู่ให้พิมพ์ "positive even."
    - ถ้าเป็นเลขคี่ให้พิมพ์ "positive odd."
 - ถ้ามีค่าน้อยกว่า 0 ให้ตรวจสอบต่อว่าเป็นเลขคู่หรือเลขคี่
    - ถ้าเป็นเลขคู่ให้พิมพ์ "negative even."
    - ถ้าเป็นเลขคี่ให้พิมพ์ "negative odd."
 - ถ้ามีค่าเท่ากับ 0 ให้พิมพ์ "zero."
"""

# input data

# input() --> str

import java.util.Scanner;
    public static void main(String args),:
        Scanner scanner = new Scanner(System.in):
        int num,result:
        for (int i = 0; i <10 ; i++):
            System.out.print("Enter integer : "):
            num = scanner.nextInt();:
    //main
    public static void checkvalue(int num):
        if(num%2==0)
            System.out.println("Even"):
        else
            System.out.println("Odd"):

    //checkvalue