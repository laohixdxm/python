#python do not support side effect of argument passing
#import pdb

def ref_demo(x):
    print ("x=",x," id=",id(x))
    x=42
    print ("x=",x," id=",id(x))

#pdb.set_trace()
x = 9
print(id(x), x)
ref_demo(x)

print(id(x), x)
