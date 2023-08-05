testing_list = [0,9,8,6,4,23,3,6,4,8,2,32,9,7,41,3,1,2,2,3,4,5,6,7,8,9,4,55,6,0,68]


def insertion(sortable):
    indexing_length = range(1, len(sortable))
    for index in indexing_length:

        while sortable[index-1] > sortable[index]:
            sortable[index], sortable[index-1] = sortable[index-1], sortable[index]
            index -= 1
    return sortable


print(insertion(testing_list))
