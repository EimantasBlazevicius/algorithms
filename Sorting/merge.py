testing_list = [0,9,8,6,4,23,3,6,4,8,2,32,9,7,41,3,1,2,2,3,4,5,6,7,8,9,4,55,6,0,68]


def merge(sortable):
    if len(sortable) > 1:
        mid = len(sortable) // 2
        left = sortable[:mid]
        right = sortable[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sortable[k] = left[i]
                i += 1
            else:
                sortable[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            sortable[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            sortable[k] = right[j]
            j += 1
            k += 1

    return sortable


print(merge(testing_list))


