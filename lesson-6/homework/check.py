def check(divided):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return divided(a, b)
    return wrapper

@check 
def div(a, b):
    return a / b

print(div(6, 2))
print(div(6, 0))