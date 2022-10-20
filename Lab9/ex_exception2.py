"""
Name: prapatsorn tempiam
ID: 364411760009
Grop: MIT421
"""

# Exception
print("Start")
while True:
    try:
        num = int(input("Enter an integer: "))
        print(f'Your number in {num}')
        break
    except ValueError as e:
        print("Error log: ",e.args)
        print("Please, enter only integer.")

print("End")