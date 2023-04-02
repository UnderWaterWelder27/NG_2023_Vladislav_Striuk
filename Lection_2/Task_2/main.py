print("\n Program is used for output only unique values from user input list")

possibly_unique_list = [lst for lst in input(" Enter element(s) and separate them by a space: ").split()]
unique_list = []

for el in possibly_unique_list:
    if el not in unique_list:
        unique_list.append(el)

print(f"\n Input element(s): {possibly_unique_list}",
      f"\n Unique element(s): {unique_list}")

