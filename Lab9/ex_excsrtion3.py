"""
Name: prapatsorn tempiam
ID: 364411760009
Grop: MIT421
"""
print("start")

def division(a,b):
    try:
        return a/b
    except:
        raise ZeroDivisionError("divide by zero")

try:
    rs = division(10,0)
    print("the result: ",rs)
except Exception as e:
    print("Error log: ",e.args)


print("End")