import math
import sys

def main():
    operators = ['+', '-', '*', '/', '%', 'sin', 'cos', 'tan']
    print()
    print("3 programs to choose from:")
    print("1) General Calculator")
    print("2) BMI Calculator")
    print("3) Converter")
    print("4) exit")
    print()

    choice = input("Choose(1 or 2 or 3 or 4): ")
    # Check if input is digit and from 1, 2, 3 or 4
    if not choice.isdigit():
        sys.exit('Choose correctly from given programs(1, 2, 3, 4)')
    choice = int(choice)
    if not (choice == 1 or choice == 2 or choice == 3 or choice == 4):
        sys.exit('Choose correctly from given programs(1, 2, 3, 4)')
    # Use Calculator for choice 1
    if choice == 1:
        print()
        print("Perform operations such as: +, -, /, *, %, sin, cos, tan")
        print("(+) for addition")
        print("(-) for subtraction")
        print("(*) for multiplication")
        print("(%) for modulo")
        print("(sin) for finding sin ratio")
        print("(cos) for finding cos ratio")
        print("(tan) for finding tan ratio")
        print()
        # Choose Operator
        operator = input("Choose Operator: ").strip()
        # Check for invalid operators
        if not operator in operators:
            sys.exit('Choose a correct operator')
        # For sin, cos, tan operator ask for mode
        if operator == 'sin' or operator == 'cos' or operator == 'tan':
            mode = input("Choose mode(r or d): ").strip().lower()
            # Check if mode is valid
            if not (mode == 'r' or mode == 'd'):
                sys.exit('Choose a correct angle mode')
            # Ask for the trignometric operand
            number = input(f"Give a number to perform {operator} on in {mode}: ")
            #Check if it is number
            try:
                number = float(number)
            except:
                sys.exit('Give a number for calculation')
            # Check for invalid tan operation with undefined angles
            try:
                result = calculator(operator=operator, first_num=number, mode=mode)
            except ValueError as e:
                sys.exit(e)
            print('Answer:', result)
            sys.exit('Program Finished!')
        # Other than sin, cos and tan operator ask for first and second operand
        print(f'For "{operator}"')
        first_number = input("Choose First Operand: ").strip()
        second_number = input("Choose Second Operand: ").strip()
        # Check if input is a number
        try:
            first_number = float(first_number)
            second_number = float(second_number)
        except ValueError:
            sys.exit("Give number for calculation")
        first_number, second_number = first_number, second_number
        try:
            number = calculator(operator, first_number, second_number)
        except ZeroDivisionError:
            sys.exit('Answer: Undefined')
        print("Answer:", number)
        sys.exit("Program Finished!")
    elif choice == 2: # Use bmi calculator for choice 2
        age = ("Give your age: ").strip()
        user_weight = ("Give your weight(Kg): ").strip()
        user_height = ("Give your height(m): ").strip()
        # Check if numerical values are given
        try:
            age = float(age)
            user_height = float(user_height)
            user_weight = float(user_weight)
        except ValueError:
            sys.exit("The info you entered isn't correct")

        if age < 14:
            sys.exit("Can't calculte BMI for age less than 14")
        if user_weight <= 0 or user_height <= 0:
            sys.exit("The info you entered isn't correct")

        bmi, status = bmi_calculator(user_weight, user_height)
        print("BMI:", bmi)
        print("Status:", status)
        sys.exit("Program Finished!")
    elif choice == 3: # Use converter
        print()
        print("1) km -> m")
        print("2) m -> km")
        print("3) kg -> lbs")
        print("4) lbs -> kg")
        print("5) °F -> °C")
        print("6) °C -> °F")
        print("7) ft -> m")
        print("8) m -> ft")
        print()

        choice = input("From the above choose conversion(1, 2, 3, 4, 5, 6, 7, 8): ")
        print()

        try:
            choice = float(choice)
        except ValueError:
            sys.exit("Choose correct option")
        
        if not choice in [1, 2, 3, 4, 5, 6, 7, 8]:
            sys.exit("Choose correct option")
        
        amount = input("Input: ")
        try:
            amount = float(amount)
        except ValueError:
            sys.exit("Invalid Input")

        if choice == 1:
            print(f'Answer: {km_to_m(amount)} m')
        elif choice == 2:
            print(f'Answer: {m_to_km(amount)} km')
        elif choice == 3:
            print(f'Answer: {kg_to_lb(amount)} lbs')
        elif choice == 4:
            print(f'Answer: {lb_to_kg(amount)} kg')
        elif choice == 5:
            print(f'Answer: {fahrenheit_to_celcius(amount)} °C')
        elif choice == 6:
            print(f'Answer: {celcius_to_fahrenheit(amount)} °F')
        elif choice == 7:
            print(f'Answer: {feet_to_meter(amount)} m')
        elif choice == 8:
            print(f'Answer: {meter_to_feet(amount)} ft')
        sys.exit("Program Finished!")
    elif choice == 4:
        sys.exit("Program Finished!")

def calculator(operator, first_num = 0, second_num = 0, mode='r'):
    match operator:
        case '+':
            return round(first_num + second_num, 1)
        case '-':
            return round(first_num - second_num, 1)
        case '*':
            return round(first_num * second_num, 1)
        case '/':
            try:
                return round(first_num / second_num, 1)
            except ZeroDivisionError:
                raise
        case '%':
            try:
                return round(first_num % second_num, 1)
            except ZeroDivisionError:
                raise
        case 'sin':
            if mode == 'r':
                return round(math.sin(first_num), 3)
            else:
                # If input is in degrees
                return round(math.sin(math.radians(first_num)), 3)
        case 'cos':
            if mode == 'r':
                return round(math.cos(first_num), 3)
            else:
                # If input is in degrees
                return round(math.cos(math.radians(first_num)), 3)
        case 'tan':
            # Assert that 90 degree and 270 degree of tan isn't defined
            # Assert that pi/2 and pi + pi/4 isn't defined
            if (first_num == 90 or first_num == 270) and mode == 'd':
                raise ValueError('infinity')
            elif ((first_num == math.pi / 2) or (first_num == math.pi + math.pi / 2)) and mode == 'r':
                raise ValueError('infinity')
            if mode == 'd':
                return round(math.tan(math.radians(first_num)), 3)
            else:
                return round(math.tan(first_num), 3)
        case _:
            return None

def bmi_calculator(weight_kg, height_m):
    bmi = round(weight_kg / (height_m * height_m), 2)

    if bmi < 18.5:
        return [bmi, 'Underweight']
    elif 18.5 <= bmi <= 24.9:
        return [bmi, 'Healthy weight']
    elif 25 <= bmi <= 29.9:
        return [bmi, 'Overweight']
    elif 30 <= bmi <= 34.5:
        return [bmi, 'Obese']
    else:
        return [bmi, 'Extremely obese']

def km_to_m(km):
    return round(km * 1000, 2)

def m_to_km(m):
    if m == 0:
        return 0
    return round(m / 1000, 3)

def kg_to_lb(kg):
    return round(kg * 2.20462, 2)

def lb_to_kg(lb):
    if lb == 0:
        return 0
    return round(lb / 2.20462, 2)

def fahrenheit_to_celcius(f):
    return round((f - 32) / 1.8, 2)

def celcius_to_fahrenheit(c):
    return round((c * 1.8) + 32, 2)

def feet_to_meter(f):
    return round(f * 0.3048, 2)

def meter_to_feet(m):
    if m == 0:
        return 0
    return round(m / 0.3048, 2)

if __name__ == '__main__':
    main()