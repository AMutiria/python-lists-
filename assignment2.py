my_list = []
my_list.append(10)
print(my_list)

my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

my_list.insert(1, 15)
print(my_list)

my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list)

del my_list[-1]
print(my_list)

my_list.sort()
print(my_list)

index_30 = my_list.index(30)
print(index_30)

