def f(x):
	return x*x

a = 0.0
b = 2.0
n = 20

dx = (b-a)/n
parc = []

for i in range(0,n):
	parc = parc + [f(a + i*dx)*dx]

print parc

upperSum = 0

for i in parc:
        upperSum += i

print (upperSum)
