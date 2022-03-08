s = set(["cat",1,2,3])
s1 =set( "".join(list(map(str,s))))
print(s1)
x = set("abcd")
y=set("bde")
z = x.union(y) - x.intersection(y)
print(z)
x.symmetric_difference_update(y)
print(x)

a = "Unestring"
print(id(a))
a += "Une autrre string"
print(id(a))