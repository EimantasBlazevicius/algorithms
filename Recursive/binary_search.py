book = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
page_we_look_for = 15


def binary_search_iter(arr, x):
    low = 0
    high = len(arr) - 1
    amount_of_times = 0

    while low <= high:
        amount_of_times += 1
        print(amount_of_times)
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def binary_search_rec(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_rec(arr, low, mid - 1, x)
        elif arr[mid] < x:
            return binary_search_rec(arr, mid + 1, high, x)
    else:
        return -1


# print(binary_search_iter(book, page_we_look_for))

print(binary_search_rec(book, 0, len(book) - 1, page_we_look_for))
