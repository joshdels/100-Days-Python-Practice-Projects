import art 

def equation(n1, n2, operation):
    if operation == '+':
        return n1 + n2
    if operation == '-':
        return n1 - n2
    if operation == '*':
        return n1 * n2
    if operation == '/':
        return n1 / n2

def calculation ():
    
    is_continue = True
    previous_number = ''
    
    print(art.logo)
    first_number = int(input("What's the first number?: "))
    operation = input("+ \n- \n* \n/ \nPick an operation: ")
    second_number = int(input("What's the second number?: "))

    previous_number = int(equation(first_number, second_number, operation))
    print(f"{first_number} {operation} {second_number} = {previous_number}")

    while is_continue:
        choice = input(f"Type 'y' to continue calculating with {previous_number}, or type 'n' to start a new equation? ")
        if choice == 'y':
            next_number = int(input("What's the next number: "))
            new_operation = input("+ \n- \n* \n/ \nPick an operation: ")
            # this is the run of the next equation
            previous_number = equation(previous_number, next_number, new_operation)
        elif choice == 'n':
            is_continue = False
            print(f"Final Number: {previous_number}")
            calculation()

# Actual Computation
calculation()
        