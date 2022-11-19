
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