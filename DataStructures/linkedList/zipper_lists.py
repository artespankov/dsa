class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_lists(head_1, head_2):
    """
    Merge lists 1 & 2
    Alternating each list's elements, in place
    """
    dummy = Node(0)
    curr = dummy
    while head_1 and head_2:
        curr.next = head_1
        curr = curr.next
        head_1 = head_1.next

        curr.next = head_2
        curr = curr.next
        head_2 = head_2.next

    if head_1:
        curr.next = head_1
    else:
        curr.next = head_2

    return dummy.next


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a -> b -> c -> d -> e -> f

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z -> d -> e -> f


w = Node("w")
# w

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3

zipper_lists(w, one)
# w -> 1 -> 2 -> 3


one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3

w = Node("w")
# w

zipper_lists(one, w)
# 1 -> w -> 2 -> 3