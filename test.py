
text = "Hellow"
mylist = []
newlist = []
i = 0
for x in text:
    mylist.append(text[i])
    i = i + 1
print(mylist)

i = 0
while i < (len(mylist)):
    if x != True:
        newlist.append(mylist[i]*3)
    else:
        print('Breaking loop')
        break
    i = i + 1
    print ('--> '+''.join(newlist))