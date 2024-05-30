class A:
    def greet(self):
        print("Hello from class A")

class B:
    def greet(self):
        print("Hello from class B")

class C(A, B):
    pass

class D(B, A):
    pass

obj1 = C()
obj1.greet()

obj2 = D()
obj2.greet()

