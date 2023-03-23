first_operand = float(input("1st operand >> "))
second_operand = float(input("2st operand >> "))

print("Choose operation: \n"
      "button (1) --- Add (+) \n"
      "button (2) --- Subtract (-) \n"
      "button (3) --- Multiply (*) \n"
      "button (4) --- Divide (/) \n")

operation = int(input(">> "))
match operation:
    case 1: print("{0} + {1} = ".format(first_operand, second_operand), str(first_operand + second_operand))
    case 2: print("{0} - {1} = ".format(first_operand, second_operand), str(first_operand - second_operand))
    case 3: print("{0} * {1} = ".format(first_operand, second_operand), str(first_operand * second_operand))
    case 4: print("{0} / {1} = ".format(first_operand, second_operand), str(first_operand / second_operand))
    case _: print("Idk what to do with this numbers, so, just look at them: {0}, {1} ")
