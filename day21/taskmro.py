class A:
    a = 2
class B(A):
    a = 20
class C(A):
    a = 200
class D(B,C):
    a = 2000
print(D.mro())      # mro = method resoltion order