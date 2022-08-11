# Statements Assessment Test
print('\n')

st = 'Print only the words that start with s in this sentence'
for letter in st.split():
    if letter[0] == 's':
        print(letter)

print('\n\n')

for i in range(0, 11):
    if (i % 2) == 0:
        print(i)

for i in range(0, 50):
    if (i % 3) == 0:
        print(i)

print('\n\n')

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    wlen = len(word)
    if (wlen % 2 == 0) == True:
        print(str(word) + '\t\t\t' + '----evenlength!')

print('\n\n')

for i in range(1, 101):
    if (i % 3) == 0:
        print(str(i) + '\t' + ' Fizz')
    if (i % 5) == 0:
        print(str(i) + '\t' + 'Buzz')
    if ((i % 5) == 0) and (i % 3) == 0:
        print(str(i) + '\t' + 'FizzBuzz')

print('\n\n')

st = 'Create a list of the first letters of every word in this string'
mylist = list()
for w in st.split():
    le = w[0]
    mylist.append(le)
print(mylist)
