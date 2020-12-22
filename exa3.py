with open("file1.txt", "r") as file1:
    # file1_data = file1.readlines()
    list1 = [int(num) for num in file1]
    print(list1)

with open("file2.txt", "r") as file2:
    list2 = [int(num) for num in file2]
    print(list2)

result1 = [n for n in list1 if n in list2]
print(result1)