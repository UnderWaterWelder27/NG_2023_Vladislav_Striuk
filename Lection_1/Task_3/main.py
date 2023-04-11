first_operand = float(input("1st operand >> "))
second_operand = float(input("2st operand >> "))
result = float()

print("Press [+], [-], [*], [/] button to confirm operation: \n"
      "[+] --- Add \n"
      "[-] --- Subtract \n"
      "[*] --- Multiply \n"
      "[/] --- Divide \n")

operation = input(">> ")
match operation:
    case '+': result = first_operand + second_operand
    case '-': result = first_operand - second_operand
    case '*': result = first_operand * second_operand
    case '/': result = first_operand / second_operand
    case _: print("Idk what to do with this numbers, so, just look at them: {0}, {1} ")

print(f"{first_operand} {operation} {second_operand} = {result}")
