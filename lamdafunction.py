def add(num):
    result = num+5
    return result
x = 5
print(add(x))

# equivalent lamda
lamda_add_5=lambda x:x+5
y =10
print(lamda_add_5(y))

lamda_concat=lambda x,y :x+y
x='kousik'
y='saikia'
print(lamda_concat(x,y))

lambda_max=lambda x,y: x if x>y else y

print(lambda_max(5,4))


# Map function

square_num = lambda x: x*x
lista = [2,3,4,5,6]
result = print(list(map(square_num,lista)))

# reduce function

import functools
add_num = lambda x,y:x+y
lista = [2,3,4,5,6]
print("the sum is ", functools.reduce(add_num,lista))

#list comprehension

lst1 = [2,1,-4,3,-5,2]

result = [x for x in lst1 if x>0]+[x for x in lst1 if x<0]
print(result)