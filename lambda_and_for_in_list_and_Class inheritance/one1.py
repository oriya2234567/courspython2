from functools import reduce
list2 = [1,2,3,4,5,12,312]
list3 = [x for x in range(1,11) if x% 2==0]

print(list3)

list12 =["12","123123","123","1","23","21","321"]
sortnum = sorted(list12, key = lambda word1: len(word1))
print(sortnum,)

list22 = [x for x in range(1,10)]
liz21= filter(lambda value:value % 2==0,list22)
print(list(liz21))

li = [1,2,3,4,5,6,7,8,9,10]
li = map(lambda j : j**2,li)
print(list(li))


li2 =[1,2,3,4]
li123 = filter(lambda k: k % 2==0,li2)
print(list(li123))



x = ["1","2","2312","321","23","90","9"]
z = sorted(x, key= lambda g : len(g))
print(z)



f =[1,2,3,4,5,3]
f2 = reduce(lambda x,y:x+y,f)###reduce functioin 
print(f2)





ch = [x for x in range(1,16)]
ch_filter = filter(lambda x : x % 2==0,ch)
print(list(ch_filter))

name = "oriya"
def foo():
    global name
    print(name)
    # global name
    name =5
    # print(name)



foo()

l = [x for x in range(1,11)]
x1 = filter(lambda x3 :x3%2==0,l)
print(list(x1))

x32 = [1,2,3,4,5,6]
v = x32.pop()
print(v)
print(x32)




def m(num):
    return "".join(sorted(set(num),key =lambda x: num.count(x),reverse=True))



def mis(n):
    return [i for i in range(n)if i %2==0]

print(mis(10))



class animal():
    def __init__(self,name,age):
         self._name = name
         self._age =age
        
    def hi(self):
        print(f"hello world my name is {self._name}")
         

class Dog(animal):
    def __init__(self,type_ofthe_dog,name,age):
        self._type = type_ofthe_dog
        super().__init__(name,age)
        print(f"hi my name is {self._name} and i am {self._age} years old and my type is {self._type}")
    
    def hi(self):
        super().hi()


rax = Dog("pomranian","rax",3)
rax.hi()



