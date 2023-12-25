class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.items[self.size()-1]


if __name__ == "__main__":
    # stack = Stack()
    # print(f"Empty: ", stack.is_empty())
    # stack.push(12)
    # stack.push("ABC")
    # print(f"Empty: ", stack.is_empty())
    # print(f"Size: ", stack.size())
    # print(f"Last Item: ", stack.peek())

    def reverse_string(string: str):
        ans = ""
        stack = Stack()
        for s in string:
            stack.push(s)
        while not stack.is_empty():
            ans += stack.pop()
        return ans

    print(reverse_string("Battle Starship Galaxy"))


    def is_valid_parentheses(string: str):
        stack = Stack()

        def par_matched(opening: str, closing: str) -> bool:
            return (opening, closing) == ("(", ")")

        for s in string:
            if s == "(":
                stack.push(s)
            else:
                if stack.is_empty() or not par_matched(opening=stack.pop(), closing=s):
                    return False
        return stack.is_empty()

    # print(is_valid_parentheses("())"))
    # print(is_valid_parentheses("((())"))
    # print(is_valid_parentheses("(())(())()"))


    def is_valid_general_parentheses(s):
        stack = Stack()
        openers = "({["
        closers = ")}]"

        def match(opening: str, closing: str) -> bool:
            return openers.index(opening) == closers.index(closing)

        i = 0
        while i < len(s):
            if s[i] in openers:
                stack.push(s[i])
            else:
                if stack.is_empty() or not match(opening=stack.pop(), closing=s[i]):
                    return False
            i += 1
        return stack.is_empty()

    print(is_valid_general_parentheses("{{([][])}()}"))
    print(is_valid_general_parentheses("[[{{(())}}]]"))
    print(is_valid_general_parentheses("[][][]()"))
    print(is_valid_general_parentheses("{}"))







