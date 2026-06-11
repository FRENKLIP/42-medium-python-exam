def merge_lists_extra(lists: list[list[int]]) -> list[int]:
    return sorted( [i for lst in lists for i in lst])
    # list_end=[]
    # for i in lists:
    #     for j in i:
    #         list_end.append(j)
    # return sorted (list_end)

lisss=[[1,2,3,4],[1,1,5,6,7],[7,8,0]]
print(merge_lists_extra(lisss))


