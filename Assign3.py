#def str1():
 #   print('football')
#    print('basketball')

#str1()

#def add(a,b):
  #   c = a + b
 #    return c
#''''''
#total = add(10,20)
#print(total)

#....
#def add(a, b):
  #  c = a * b
 #   return c
#...

#multi = add(10, 'vijay')..
#print(multi)...
#''''''#
''''
def add1(x,y):
    print(x+y)

add1(10,20)
'''
'''''
def add(x,y):
    return x + y
def square(z):
    return z * z

result= square(add(6,1))
print(result)
'''
'''''
import math
print (math.pi)
'''
'''''
def python():
    print("python")
    python()

python()
'''
'''
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

n = 0
def python():
    global n
    n= n + 1
    print("python",n)
    python()

python()
'''
'''''
def factorial(n):
    if n< 2:
        return(1)
    else:
        return n * (factorial(n-1))

result = factorial(17)
print(result)
'''
'''''
n = 1


def fn():
    global n
    n = 5
    print('in',n)
fn()

print('out',n)
'''

#1

def factorial(n):
    if (n<2):
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)

#2

a = int(input('enter the number: '))
import math
sqrt = math.sqrt(a)
lg = math.log(a)
sine = math.sin(a)
print(f'Square root: {sqrt}')
print(f'Logarithm: {lg}')
print(f'sine: {sine}')







