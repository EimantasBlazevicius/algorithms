testing_list = [0,9,8,6,4,23,3,6,4,8,2,32,9,7,41,3,1,2,2,3,4,5,6,7,8,9,4,55,6,0,68]


def bubble(list_to_sort):
    indexing_length = len(list_to_sort)-1
    sorted = False
    while not sorted:
        sorted = True
        for index in range(0, indexing_length):
            if list_to_sort[index] > list_to_sort[index+1]:
                sorted = False
                list_to_sort[index], list_to_sort[index+1] = list_to_sort[index+1], list_to_sort[index]
    return list_to_sort


print(bubble(testing_list))