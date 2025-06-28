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