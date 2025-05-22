from sympy import Symbol, expand
x = Symbol('x')
f = x + x + x + 2
print(f) 

#
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
s = x*y + y*x 
print(s)

#
p = x*(x+2*x)
print(p)

p1 = (x+2)*(y+3)
print(p1)
p2 = (x+2)*(y+3) + (x+2)*(x-3)
print(p2) 

p3 = (x+2)*(y+3)
print(p3.expand())

#2.2.1
from sympy import factor, expand
bieuthuc1 = x**3 - y**3
print(factor(bieuthuc1))

bieuthuc2 = (x-y)*(x**2 + x*y + y**2)
print(expand(bieuthuc2))

#2.2.3
x = Symbol('x')
y = Symbol('y')
bieuthuc3 = x*x - x*y + y*y
print(bieuthuc3)

giatri = bieuthuc3.subs({x:3, y:2}) 
print(giatri)

