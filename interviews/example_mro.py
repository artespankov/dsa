class A:
    def say(self):
        print(" In class A")


class B(A):
    def say(self):
        print(" In class B")


class C(A):
    def say(self):
        print("In class C")


# classes ordering
class D(B, C):
    pass


if __name__ == "__main__":
    d = D()
    d.say()
