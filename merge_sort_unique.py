def merge_sort_unique(lists):
    return sorted(set(num for lst in lists for num in lst))


lists = [[1, 3, 5], [2, 3, 6], [1, 7]]
print(merge_sort_unique(lists))
