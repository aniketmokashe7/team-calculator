import math

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take sqrt of negative number")
    return math.sqrt(x)

def power(base, exp):
    return base ** exp

def percentage(part, whole):
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100

if __name__ == "__main__":
    print("sqrt(9) =", sqrt(9))