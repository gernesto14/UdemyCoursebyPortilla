#Importing OS module
import os


# print(os.getcwd())
print(os.listdir())


# addnote = "This is my first line"
# myfile.write(addnote)

userinput = True
while userinput is not False:
    userinput = input("\nEnter operation:\n "
                      "\t'0' ends loop"
                      "\t'1' continue ")




    if userinput == '0':
        break




