# python calculator

def calculate(num1, num2, operation):

    if operation == "+":
        add = num1 + num2
        print(add)

    elif operation == "-":
        sub = num1 - num2
        print(sub)

    elif operation == "*":
        mul = num1 * num2
        print(mul)

    elif operation == "/":
        div = num1 / num2
        print(div)
    
calculate(2, 4, "+")
calculate(8, 4, "-")
calculate(5, 2, "*")
calculate(15, 5, "/")