def add(num1: int, num2: int):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "ensure parameters are integers"
    
    return num1 + num2

def subtract(num1: int, num2: int):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "ensure parameters are integers"

    return num1 - num2

def divide(num1: int, num2: int):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "ensure parameters are integers"

    try:
        return num1/num2
    except ZeroDivisionError:
        return "can't divide by 0"

def sqrt(num1: int):
    if not isinstance(num1, int):
        return "ensure parameters are integers"
    
    if num1 < 1:
        return "num must be > 0"
    return num1 ** 0.5