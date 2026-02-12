class A:
    def show(self):
        print("A")
        super().show()

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.show()
