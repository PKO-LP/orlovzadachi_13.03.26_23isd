h = int(input())
m = int(input())
s = int(input())
h1 = int(input())
m1 = int(input())
s1 = int(input())

t1 = h * 3600 + m * 60 + s
t2 = h1 * 3600 + m1 * 60 + s1

delta = t2 - t1
print(delta)