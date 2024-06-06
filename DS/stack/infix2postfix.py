from DS.stack.Stack import Stack


def infix_to_postfix(infixexpr):
    precision = {
        "**": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }
    op_stack = Stack()
    postfix_list = []
    token_list = infixexpr.split()
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while not op_stack.is_empty() and precision[op_stack.peek()] >= precision[token]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


if __name__ == "__main__":
    # print(infix_to_postfix("A * B + C * D"))
    # print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # #
    # print(infix_to_postfix("( A + B ) * ( C + D )"))
    # # 'A B + C D + *'
    # print(infix_to_postfix("( A + B ) * C"))
    # # 'A B + C *'
    # print(infix_to_postfix("A + B * C"))
    # # 'A B C * +'
    print(infix_to_postfix("5 * 3 ** ( 4 - 2 )"))
