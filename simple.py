ef calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "Invalid operator"
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")
print(calculator(x, y, op))
