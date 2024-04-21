# 2 Завдання "Калькулятор"
# Реалізуйте функцію, яка обчислює значення виразу, поданого у
# польській(постфіксній) нотації. Використайте функцію з уроку

def evaluate_expression(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            try:
                operand2 = stack.pop()
                operand1 = stack.pop()
            except IndexError:
                raise ValueError("Invalid expression")

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
            else:
                raise ValueError("Invalid token: {}".format(token))

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid expression")
expression = "3 4 + 2 *"
result = evaluate_expression(expression)
print("Результат обчислення:", result)




