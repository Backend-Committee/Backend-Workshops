def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."