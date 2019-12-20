import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# current operation is O(n^2)
# Should be a total of 64 duplicates, current runtime is 12 seconds
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ***************************************************************************
# 64 duplicates were found, under 1 sec run time
duplicates = []
names_bst = BinarySearchTree('')

for name_1 in names_1:
    names_bst.insert(name_1)

for name_2 in names_2:
    if names_bst.contains(name_2):
        duplicates.append(name_2)

# ***************************************************************************
print(duplicates)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
