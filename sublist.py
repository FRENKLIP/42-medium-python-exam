def sublist(lst: list[int], k: int) -> list[int]:
    n = len(lst)
    newList = []

    for i in range(n):
        if n - i < k:
            break
        newList.append(max(lst[i:k+i]))

    return newList
# print(sublist([1, 2, 3, 4, 5], 2))  # Output: [2, 3, 4, 5]
# print(sublist([5, 4, 3, 2, 1], 3))  # Output: [5, 4, 3]
# print(sublist([1, 3, 2, 5, 4], 1))  # Output: [1, 3, 2, 5, 4]
