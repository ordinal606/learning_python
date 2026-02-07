"""
CLI Calculator.

Supports basic arithmetic operations:
addition, subtraction, multiplication, and division.

Handles invalid input and division by zero gracefully.
"""

def get_number(prompt: str) -> float:
    """
    Prompt the user for a number and validate input.
    """
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid input. Try again.")

def get_operator() -> str:
    """
    Prompt the user to enter an operator and validate input.
    """
    prompt = "Enter an operator (+, -, *, /)> "
    invalid_input_msg = "Invalid operator. Try again."
    operators = ["+", "-", "*", "/"]

    while True:
        s = input(prompt).strip()

        if s not in operators:
            print(invalid_input_msg)
        else:
            break

    return s

def calculate(a: float, operator: str, b: float) -> float:
    """
    Does addition, subtraction, multiplication, and division for floats.
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero.")
        else:
            return a / b

def main() -> None:
    welcome_msg = "Welcome to the CLI Calculator.\n"

    first_number_prompt = "Enter the first number> "
    second_number_prompt = "Enter the second number> "

    repeat_prompt = "\nPerform another calculation? (y/n)> "

    terminate_msg = "\nGoodbye."

    print(welcome_msg)

    repeat = True
    while repeat:
        a = get_number(first_number_prompt)
        operator = get_operator()
        b = get_number(second_number_prompt)

        try:
            result = calculate(a, operator, b)
        except ZeroDivisionError as e:
            print(e)
            continue

        result_string = f'\nResult: {a} {operator} {b} = {result}'
        print(result_string)

        while True:
            r = input(repeat_prompt).strip()
            if r == 'n':
                repeat = False
                break
            elif r == 'y':
                break

    print(terminate_msg)

if __name__ == "__main__":
    main()
