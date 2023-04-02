print("\n Program is used to get non-unique values from every of three lists, "
      "and output unique values from all of this three lists"
      "\n Enter element(s) and separate them by a space: ")

possibly_unique_list_1 = [lst for lst in input("First set: ").split()]
possibly_unique_list_2 = [lst for lst in input("Second set: ").split()]
possibly_unique_list_3 = [lst for lst in input("Third set: ").split()]

unique_duplicates_1 = list({el for el in possibly_unique_list_1 if possibly_unique_list_1.count(el) > 1})
unique_duplicates_2 = list({el for el in possibly_unique_list_2 if possibly_unique_list_2.count(el) > 1})
unique_duplicates_3 = list({el for el in possibly_unique_list_3 if possibly_unique_list_3.count(el) > 1})

print(f"\n Unique duplicates: {list(set(unique_duplicates_1 + unique_duplicates_2 + unique_duplicates_3))}")
