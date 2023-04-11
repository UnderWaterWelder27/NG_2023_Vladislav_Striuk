def actionMenu():
    print("Press [+], [-], [*], [/] button to confirm operation: \n"
          "[+] --- Add \n"
          "[-] --- Subtract \n"
          "[*] --- Multiply \n"
          "[/] --- Divide \n")


def inputOperation():
    return input(">> ")


def calculateOperands(op_1, op_2, operation):
    match operation:
        case '+': return op_1 + op_2
        case '-': return op_1 - op_2
        case '*': return op_1 * op_2
        case '/': return op_1 / op_2
        case _: return 'NO RESULT (a vot because you entered wrong operation)'


def outputResult(res):
    print(f"Result: {res}")


def main():
    first_operand = float(input("1st operand >> "))
    second_operand = float(input("2st operand >> "))

    actionMenu()
    operation = inputOperation()
    result = calculateOperands(first_operand, second_operand, operation)

    outputResult(result)


if __name__ == '__main__':
    main()
