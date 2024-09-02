"""
Complete the code below to print following result
A B
A B
class A:
 def f(self):
 return self.g()
 def g(self):
 <<<<Place Your Code Here>>>>
class B(A):
 def g(self):
 <<<<Place Your Code Here>>>>
a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())
"""
class A:
    def f(self):
        return self.g()
    def g(self):
        return "A"

class B(A):
    def g(self):
        return "B"

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())