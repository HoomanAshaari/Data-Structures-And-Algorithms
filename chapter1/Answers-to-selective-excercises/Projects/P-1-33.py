def calculator():
    print("Enter your operation: (use ctrl+C to RESET)")
    try:
        num1 = int(input("First number: "))
        operator = input("Operator: ")
        num2 = int(input("Second number: "))

        if operator == '+':
            result = num1+num2
        elif operator == '-':
            result = num1-num2
        elif operator == '*':
            result = num1*num2
        elif operator == '/':
            result = num1/num2
        else:
            print("Wrong operator imported! Try again")
            calculator()
        
        print(num1, operator, num2, '=', result)

    except KeyboardInterrupt:
        calculator()


calculator()
