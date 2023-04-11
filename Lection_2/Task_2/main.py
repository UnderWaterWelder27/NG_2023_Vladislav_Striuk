print("\n Program is used for output only unique values from user input list")

possibly_unique_list = [lst for lst in input(" Enter element(s) and separate them by a space: ").split()]

print(f"\n Input element(s): \n {possibly_unique_list} ",
      f"\n Unique element(s): \n {set(possibly_unique_list)}")
