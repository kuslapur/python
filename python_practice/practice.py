"""
def foo(x=[]):
    x.append(1)
    return x
print(foo())


str = input("enter the string")
rev_string = str[::-1]
print(f"the given string is ", {str}, "and the revers string is ",{rev_string})


n = int(input("enter the no"))

if n == 1:
    print("given no is 1")
elif n == 2:
    print("given no is 2")
else:
    print("its other")



def fun():
    name = "alice"
    age  = 35
    return name, age
name,age = fun()
print(name,age)



def trickey_fun(a, b=[]):
    b.append(a)
    return b
print(trickey_fun(1))
print(trickey_fun(2))
"""
