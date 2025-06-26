x = [z for z in range(0,10)if z % 2==0]
print(x)
number =[1,2,3,4,5,6,7,8,9,10]
x = filter(lambda x: x%2==0 ,number)
print(list(x))


