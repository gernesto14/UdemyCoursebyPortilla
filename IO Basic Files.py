#Importing OS module
import os

#
# # my file = open('test.txt')
# print('\nPrint current working directory')
# print(os.getcwd())
#
# print('\n')
# #Changing directory path
# os.chdir('/Users/Ernesto Garcia/Documents/Programming/Python/Class/')
#
# print('\n')
# #List all files in that folder
# print(os.listdir())
#
# #Create new file
# # os.mkdir('New Folder Test')
# #Delete folder/file
# #os.rmdir('New Folder Test')

# os.chdir('/Users/Ernesto Garcia/Documents/Programming/Python/Class/Udemy Course by Portilla')
# print('\n')
# print('List of all files: \n')
# #List all files in that folder
# print(os.listdir())
#
# myfile = open('\\Users\\Ernesto Garcia\\Documents\\'
#               'Programming\\Python\\Class\\Udemy Course by Portilla\\test.txt')
#
# myfile = open('test.txt', 'r')
#
#
#
# myfile = open('test.txt', mode = 'r')
#


print(os.getcwd())
print(os.listdir())

myfile = open('test1', 'r', encoding='cp1252')

print(myfile)