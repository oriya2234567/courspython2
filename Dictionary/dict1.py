d = {
    "oriya" : 16,
    "nadav" :11,
    "shlomi": 21
}
d = dict(sorted(d.items(),key = lambda item: item[1]))
print(d)