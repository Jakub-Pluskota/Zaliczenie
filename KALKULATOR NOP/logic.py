def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

import re

def tokenize(expression):
    return re.findall(r'\d+\.\d+|\d+|[()+\-*/]', expression)

def infix_to_rpn(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []
    tokens = tokenize(expression)

    for token in tokens:
        if token.isnumeric() or is_float(token):
            output.append(token)
        elif token in precedence:
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if operators and operators[-1] == '(':
                operators.pop()
            else:
                raise ValueError("Brak nawiasu otwierającego")

    while operators:
        if operators[-1] in '()':
            raise ValueError("Brak nawiasu zamykającego")
        output.append(operators.pop())

    return output

def evaluate_rpn(tokens):
    stack = []
    for token in tokens:
        if token in '+-*/':
            if len(stack) < 2:
                return "Błąd składni"
            b = stack.pop()
            a = stack.pop()
            try:
                result = perform_operation(a, b, token)
            except ZeroDivisionError:
                return "Dzielenie przez zero"
            stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                return "Nieprawidłowa liczba"

    if len(stack) != 1:
        return "Błąd składni"
    return stack[0]

def perform_operation(a, b, operator):
    if operator == '+': return a + b
    if operator == '-': return a - b
    if operator == '*': return a * b
    if operator == '/': return a / b