def find_intersection_union(list1, list2):
    intersection = list(set(list1) & set(list2))
    union = list(set(list1) | set(list2))
    return intersection, union

# Sample input lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find intersection and union
intersection, union = find_intersection_union(list1, list2)

# Output
print("List 1:", list1)
print("List 2:", list2)
print("Intersection:", intersection)
print("Union:", union)
