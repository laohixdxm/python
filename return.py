#without side effect of argument passing, python support multiple return

def f(x,y):
    x,y=2,1
    return x,y


a,b=1,2
print(a,b)
a,b = f(a,b)
print(a,b)