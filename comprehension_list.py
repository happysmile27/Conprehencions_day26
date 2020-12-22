number = [1, 2, 3]
# new_list = [new_item for item in list]
new_list = [n + 1 for n in number]
print(new_list)

range(1, 5)
double_range = [n * 2 for n in range(1, 5)]
print(double_range)

names = ["Alex", "Olia", "Volodymyr", "Olenka", "Ave"]
new_names = [name for name in names if len(name) <= 4]
capitalized = [name.upper() for name in names if len(name) >= 5]
print(capitalized)
print(new_names)