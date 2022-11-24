# write a list comprehension program to print 10 numbers

result = [x for x in range(1,11)]
print(result)


result1= [x for x in range(1,51) if x%2==0]
print(result1)

list1 = ['hello','my', 'name' , ' is' , 'kousik']
# Using map 
print(list(map(lambda x :x.upper(), list1)))

# using list comprehension

print([x.upper() for x in list1])


list2 = [3,-1,2,-7,5,-8,9]

# Using filter
print(list(filter(lambda x:x>=0, list2))+list(filter(lambda x: x<0, list2)))

# using list comprehension

print([x for x in list2 if x >= 0 ] + [x for x in list2 if x < 0])

# sorting 
results = [x for x in list2 if x >= 0 ] + [x for x in list2 if x < 0]
results.sort()
print(results)


