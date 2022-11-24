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