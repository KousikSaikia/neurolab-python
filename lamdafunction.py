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