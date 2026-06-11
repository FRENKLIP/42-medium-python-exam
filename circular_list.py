def circular(lst1: list[int], lst2: list[int]) -> bool:
    if len(lst1) != len(lst2):
        return False

    if lst1 == lst2:
        return True

    for _ in lst1:
        value = lst2.pop()
        lst2.insert(0, value)

        if lst1 == lst2:
            return True

    return False
#pythonmedium