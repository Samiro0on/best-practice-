# The mode is the number that occurs most often within a set of numbers.

from collections import Counter

    # list of elements to calculate mode
n_num = [1, 4, 5, 2, 3, 4, 5, 5]
n = len(n_num)

data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is: " + ', '.join(map(str, mode))

print(get_mode)
