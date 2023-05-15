# multiple
class A:
    a = 1
class B:
    a = 2
class C(A,B):
    pass
obj = C()
print(obj.a)

# multilevel
class A:
    a = 1
class B(A):
    a = 2
class C(B):
    pass
obj = C()
print(obj.a)

# hierarchical
class A:
    a = 1
class B(A):
    a = 2
class C(A):
    a = 3

# hybrid inheritance
class D:
    a = 22
class E:
    a = 23
class A(D,E):
    a = 1
class B(A):
    a = 2
class C(A):
    a = 3
    print(C.mro())