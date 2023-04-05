def run(operations: dict):
    while True:
        operation = input(">>>")
        if operation not in operations:
            print("Not supported operation!")
            continue
        operand1 = int(input())
        operand2 = int(input())

        print(f"Result: {operations[operation](operand1, operand2)}")