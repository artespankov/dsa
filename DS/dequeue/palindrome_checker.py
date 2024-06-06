from DS.dequeue.Dequeue import Dequeue


def palindrome_checker(string: str):
    dequeue = Dequeue()

    for ch in string:
        dequeue.add_rear(ch)

    while dequeue.size() > 1:
        if dequeue.remove_front() != dequeue.remove_rear():
            return False
    return True


if __name__ == "__main__":
    print(palindrome_checker("vanillaallinav"))
    print(palindrome_checker("lsdkjfskf"))
    print(palindrome_checker("radar"))