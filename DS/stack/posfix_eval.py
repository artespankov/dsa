from DS.stack.Stack import Stack


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        elif token in "+-*/":
            # left operand is on bottom as it was pushed fist, like in A / B
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            operand_stack.push(do_math(token, left_operand, right_operand))

    return int(operand_stack.pop())


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


if __name__ == "__main__":
    print(postfix_eval('7 8 + 3 2 + /'))
