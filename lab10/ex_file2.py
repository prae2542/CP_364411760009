"""
Name: prapatsorn tempiam
ID: 364411760009
Grop: MIT421
"""

# create file

# create empty file
#try:
    #f = open("test2.txt","x")
#except:

    #print("file already exits.")

#create text3.txt on desktop of your computer
#C:\Users\LabCom_MT-4\Desktop
import os

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\test3.txt","x")
    f.close()
except Exception as e:
    print(e)


# write file
#mode "a" , "w"
try:
    f = open("test2.txt","w")
    f = write("prapatsorn tempiam")
except:
    print("cloud not found a fine name 'trst2.txy")
finally:
    f.close()

# delete file

if os.path.exists("test3.txt")
os.remove("test2.txt")
else:
    print("file not found.")

