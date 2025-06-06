import math

def basic_arithmetic():
    print("Basic Arithmetic:")
    a, b = 6, 9
    print(f"a = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")

def builtin_functions():
    print("\nBuilt-in Math Functions:")
    numbers = [1, -5, 3.14, -2.5, 7]
    print(f"Numbers: {numbers}")
    print(f"Absolute value of -5: {abs(-5)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Round 3.14 to 1 decimal place: {round(3.14, 1)}")

def trigonometry():
    print("\nTrigonometric Functions:")
    angle = math.pi / 4  # 45 degrees
    print(f"Angle: {angle} radians ({math.degrees(angle)} degrees)")
    print(f"Sine: {math.sin(angle)}")
    print(f"Cosine: {math.cos(angle)}")
    print(f"Tangent: {math.tan(angle)}")

def logarithmic():
    print("\nLogarithmic Functions:")
    x = 10
    print(f"Natural logarithm of {x}: {math.log(x)}")
    print(f"Base-10 logarithm of {x}: {math.log10(x)}")
    print(f"Exponential (e^x) of 2: {math.exp(2)}")

def misc_math():
    print("\nMiscellaneous Math Functions:")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"GCD of 48 and 18: {math.gcd(48, 18)}")
    print(f"Ceiling of 3.7: {math.ceil(3.7)}")
    print(f"Floor of 3.7: {math.floor(3.7)}")

def main():
    basic_arithmetic()
    builtin_functions()
    trigonometry()
    logarithmic()
    misc_math()

if __name__ == "__main__":
    main()
