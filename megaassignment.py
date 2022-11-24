
# Q76. Write a Python program to find the factorial of a given number.

x = 5 
result = 1
for x in range(1,x+1):
    result = result * x
print(result)



# # Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100

def simpleInterest(p,r,t):
    SI = (p*r*t)/100
    print(SI)

princial = float(input("Enter the principal amount : "))
roi = float(input("Enter the rate of interest : "))
time = float(input("Enter the number of years : "))

simpleInterest(princial, roi, time)

# # Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

def CompundInterest(p,r,t):
    CI = p*((1+r/100)**t)
    print(CI)

princial = float(input("Enter the principal amount : "))
roi = float(input("Enter the rate of interest : "))
time = float(input("Enter the number of years : "))

CompundInterest(princial, roi, time)


# Q79. Write a Python program to check if a number is prime or not.

number = int(input("Enter a whole number greater than one: "))
flag = False
for x in range(2,number):
    print(x)
    if number%x==0:
        flag = True
        break
if flag ==True:
    print('No is not a prime number')
else:
    print('No is a prime number') 

    


# Q80. Write a Python program to check Armstrong Number.

number = input("Enter a whole number greater than one: ")
#str_num=str(number)
lst_num = list(number)

import functools

sum = functools.reduce(lambda x,y:x+y, list(map(lambda x: int(x)**3, lst_num)), 0)

if sum==int(number):
    print('this is armstrong number')
else:
    print('This is not a armstrong number')

# Q81. Write a Python program to find the n-th Fibonacci Number.

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return (0) 
    
    elif n==1: 
        return (1)
    else:
        return (Fibonacci(n-1)+Fibonacci(n-2)) 
print(Fibonacci(3)) 

# Q82. Write a Python program to interchange the first and last element in a list.

list1= [1,2,3,4]
num=list1[-1]
list1[-1]=list1[0]
list1[0]=num
print(list1)

# Q83. Write a Python program to swap two elements in a list.

list1= [81,31,3,45,86,21,33,25]
val1 = 33
val2 = 45
idx1 = list1.index(val1)
idx2 = list1.index(val2)

list1[idx1] = val2
list1[idx2] = val1

print(list1)

# Q84. Write a Python program to find N largest element from a list.

list1= [81,25,3,45,86,21,33,25]
N = 4
list1.sort(reverse=False)
for x in range(1,N+1):
    print(list1[-x])

# Q85. Write a Python program to find cumulative sum of a list.
import functools
print(functools.reduce(lambda x,y:x+y, list1, 0))

# Q86. Write a Python program to check if a string is palindrome or not.

str1 = 'malayalam'
list1 = list(str1)
print(list1)
print(list1[::-1])
if list1 == list1[::-1]:
    print('This a pallindrome')
else:
    print('Not a pallindrome')

# Q87. Write a Python program to remove i'th element from a string.

str1='hello world'
n = 3
str1=str1.replace(str1[n], '')
print(str1)

# Q88. Write a Python program to check if a substring is present in a given string.

str1 = 'this is my play ground and I play cricket here everyday'
substr = 'ket'
if str1.find(substr)!=-1:
    print('Substring is present')
else:
    print('Substring is absent')

# Q89. Write a Python program to find words which are greater than given length k.

str1 = 'this is my play ground and I play cricket here everyday'
n = 4
lst1=str1.split()
print(list(x for x in lst1 if len(x)>4))

# Q90. Write a Python program to extract unquire dictionary values.

dict1 ={'name': 'kousik', 'age': 35, 'city': 'Hyderabad', 'exp': 12,'logic':'kousik'}

print(set(dict1.values()))
# Q91. Write a Python program to merge two dictionary.

dict1 = {'name':'kousik','age':35}
dict2 = {'city':'Hyderabad','exp':12}

dict1.update(dict2)
print(dict1)
# Write a Python program to create a list of tuples from given list having number and its cube in each tuple.

list1 = [9,5,6]

lambda_cube = lambda x:x*x*x
lst1 =[]
for x in list1:
    tup= (x,lambda_cube(x))
    lst1.append(tup)
print(lst1)

#Write a Python program to convert a list of tuples into dictionary.

lst1 = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
dict3 = {}
for x,y in lst1 :
    dict3[x]=y

print(dict3)

#Write a Python program to create a list of tuples from given list having number and its cube in each tuple
list = [9, 5, 6]

print([(x,x**3) for x in list])

#Write a Python program to get all combinations of 2 tuples.

test_tuple1 = (7, 2)
test_tuple2 = (7, 8)

result1 = [(x,y) for x in test_tuple1 for y in test_tuple2]
result2 = [(x,y) for x in test_tuple2 for y in test_tuple1]
print(result1+result2)

# Write a Python program to sort a list of tuples by second item.

list1= [('for', 24), ('Geeks', 8), ('Geeks', 30)] 

reslt = []
print(type(reslt))
for x,y in list1:
    print(y)
   # reslt.sort()
reslt.sort()


list1.sort(reverse=False,key=lambda x: x[1])
print(list1)




for x in range(1,6):
    print('* '*x)


for y in range(1,6):
    print(((5-y)*' ')+'*'*y)


for x in range(1,6):
    for y in range(1,x+1):
        print(y, end=" ")
    print(" ")


x = 5
for i in range(x):
    for j in range(x):
        print(end=" ")
    x = x - 1
    for j in range(i + 1):
        print("* ", end=' ')
    print(" ")


list1 = ['A','B','C','D','E']

for x in range(len(list1)):
    for y in range(x+1):
        print(list1[x],end=' ')
    print('')