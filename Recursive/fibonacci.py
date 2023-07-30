#  0,1,1,2,3,5,8,13,21,34,55,89,144,233,377
import time
# import sys
#
# sys.setrecursionlimit(99)


def fibonacci_iter(amount_of_times):
    times = range(amount_of_times)
    result = []
    for index in times:
        if index == times[0]:
            result.append(0)
        elif index == times[1]:
            result.append(1)
        else:
            result.append(result[index-1] + result[index-2])
    return result[-1]


# for n in range(1, 99):
#     print(f"{n}: {fibonacci_iter(n)}")


def fibonacci_rec(amount_of_times, memory={}):
    if amount_of_times == 1:
        return 1
    elif amount_of_times == 2:
        return 1
    elif amount_of_times > 2:
        if amount_of_times in memory:
            return memory[amount_of_times]
        memory[amount_of_times] = fibonacci_rec(amount_of_times-1) + fibonacci_rec(amount_of_times-2)
        return memory[amount_of_times]


for n in range(1, 99):
    start = time.perf_counter()
    print(f"{n}: {fibonacci_rec(n)}")
    finish = time.perf_counter()
    print(round((finish - start)*100000, 3))
