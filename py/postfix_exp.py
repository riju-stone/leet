def evalPostfix(tokens):
    operators = "+-*/"
    exp_stack = []

    for c in tokens:
        if c not in operators:
            exp_stack.append(c)
        else:
            operand1 = str(exp_stack.pop())
            operand2 = str(exp_stack.pop())

            temp_exp = operand2 + c + operand1

            print(f"Temp Exp: {temp_exp}")

            exp = int(eval(temp_exp))
            exp_stack.append(exp)

    return int(exp_stack[0])


if __name__ == "__main__":
    res = evalPostfix(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
    print(res)

    res2 = evalPostfix(["4", "13", "5", "/", "+"])
    print(res2)
