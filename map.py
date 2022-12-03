list1=[1,2,3,4,5,6]



lst2 = list(map(lambda x:x*x, list1))
print(list1)
print(lst2)


print(list(map(lambda a,b:a+b,list1,lst2)))

list3=[1,5,3]
import functools

add_num = lambda x,y:x+y
print(functools.reduce(add_num, list3, 0))


print(list(filter(lambda x:x%2!=0, list1)))


set1 = {1,2,3,4,5,6}
set2={4,5,6,7,8,9}

print(set1 | set2)

print(set1 & set2)

var1 ={'Sachin': 10, 'Rohit': 45}
var2={'MSD': 7, 'Kohli': 18}
var1.update(var2)

print(var1)
k1=var1.keys()
for x in k1:
    print(var1[x])

for x in range(1,6):
    print('* '*x)

for y in range(1,6):
    print(((5-y)*' ')+'*'*y)

for x in range(1,6):
    for y in range(1,x+1):
        print(y, end=" ")
    print(" ")

