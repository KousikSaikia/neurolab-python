
#Write a Python program to merge two dictionary.
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