# Importing OS module
import os

print(os.listdir())  # Print directory list files

userinput = True
count = 0
while userinput is not False:

    newline = "{} line\t".format(count)
    userinput = str(input("\nEnter operation:\n "
                          "\t'0' ends "
                          "\t'1' continue "
                          "\t'W' write new line"
                          "\t'R' read\t"
                          "\t'A' append"))

    if userinput == '0':
        break
    elif userinput == 'w':
        with open('test.txt', mode='w+') as f:
            contents = f.write('\n' + newline)
            print(contents)

    elif userinput == 'r':
        with open('test.txt', mode='r') as f:
            contents = f.read()
        print(contents)

    elif userinput == 'a':
        with open('test.txt', mode='a') as f:
            contents = f.write('\t' + newline)
            print(contents)
    count = count + 1

# Creating new branch from Intellij
# Second time
