"""
    Move all zeros to end of the List
    example list1 = [1, 3, 0, 4, 5, 0, 7, 0]
    expected_result = [1, 3, 4, 5, 7, 0, 0, 0]
"""

list1 = [1, 3, 0, 4, 5, 0, 7, 0]

for item in list1:
    if item == 0:
        list1.remove(item)
        list1.append(item)

print(list1)