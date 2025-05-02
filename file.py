'''
file1 = open('my_file.txt','w')
reading_file = file1.read()
print(reading_file)
file1.close()
'''
from fileinput import filename
from random import sample

'''
with open('my_file.txt','r') as file1:
    reading_file = file1.read()
    print(reading_file)

'''
#with open('my_file.txt','w') as file1:
'''''
file1 = open ('my_file.txt','w')
writing_file = file1.write('hello')
print(writing_file)
file1.close()

file1 = open('my_file.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()

file1 = open('my_file.txt','a')
appending_file = file1.write('welcome to the lecture')
print(appending_file)
file1.close()

file1 = open('my_file.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()
'''
'''''
file = open('my_file.txt','r+')
w_f = file.write('welcome')
print(w_f)
file.close()

file = open('my_file.txt','r+')
r_f = file.read()
print(r_f)
file.close()
'''
'''''
file = open('sample.txt','r')
reading_file = file.read()
print(reading_file)
file.close()
'''''

def read_file(sample):
    try:
        with open(sample, 'r') as file:
            print("File content:")
            for line in file:
                print(line, end='')  # end='' to avoid extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{sample}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

result = read_file(sample)
print(result)


