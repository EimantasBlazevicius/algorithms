testing_list = [0,9,8,6,4,23,3,6,4,8,2,32,9,7,41,3,1,2,2,3,4,5,6,7,8,9,4,55,6,0,68]


def quick_sort(sortable):
    length = len(sortable)
    if length <= 1:
        return sortable
    else:
        pivot = sortable.pop()

        items_greater = []
        items_lower = []

        for item in sortable:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort(testing_list))
