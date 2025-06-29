from functools import reduce

d = {
    "oriya" : 16,
    "nadav" :11,
    "shlomi": 21
}
d = dict(sorted(d.items(),key = lambda item: item[1]))
print(d)



d ={
 "oriya": 10,
 "noam" :1,
 "shalom": 121

   }
print(d)
list_of_value = d.values()
list_of_keys = d.keys()
list_of_items = list(d.items())

print(list_of_value)
print(list_of_keys)
print(list_of_items[2])

li = {
    "name": 17,
    "age": 15,
    "age2":122,
    "name2": 27,
    "age2": 200,
    "age2":13

    }
li = list(li.items())
li = sorted(li, key= lambda item:item[1])
li = dict(li)

print(li)



liz = {
    "name": 17,
    "age": 15,
    "age2":122,
    "name2": 27,
    "age2": 200,
    "age2":13,
    "name3": 17,
    "age3": 15,
    "age3":122,
    "name3": 27,
    "age3": 200,
    "age3":13

    }
print(liz)
liz = list(liz.items())
liz = sorted(liz,key= lambda x: x[1])
liz = dict(liz)
print(liz)



string3 = "hi my name is oriya and i love to eat pizza and see footbal"
string3 =string3.split()
print(string3)
string3 = string3.reverse()
print(string3)
s =[1,2,3,4]
d = s
d.append(5)
print(s)
print(s[-1::-1])
s =[1,2,3,45,12,3,1,45,2]
s = list(set(s))
print(s)


def mul(number):
    if number == 0 or number ==1:
        return 1
    else:
        return number * mul(number-1)
    
# print(mul(5))

def mul2(number):
    sum =1
    end = number 
    count =0
    while count < end:
        sum *= number
        number = number-1
        count+=1
    return sum

print(mul2(8))


def th(num):
    liz42= [l for l in range(1,num+1)]
    return reduce(lambda x ,y : x * y,liz42)
   

print(th(5))