tuple = ('a', 100, "abc", 100.10, True)
tuple1 = ('b', 40, "abhi", 100.10, False)

print(tuple)
print(tuple[1])
print(tuple[1:4])
print(tuple[1:])
print(tuple[:4])
print(tuple[:])
newtuple = tuple * 2
print(newtuple)
t3 = tuple + tuple1
print(t3)
print(len(t3))
print(tuple.count(100.10))
print(tuple.index("abc"))
print(tuple1.index(100.10))

print(tuple1.index(100.10, 3))

