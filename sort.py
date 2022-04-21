def bubble_sort(arr):

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x += 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
                return arr

    return arr


def cycle_sort(arr):
    len_arr = len(arr)

    for cur in range(len_arr - 1):
        item = arr[cur]

        index = cur
        for i in range(cur + 1, len_arr):
            if arr[i] < item:
                index += 1

        if index == cur:
            continue

        while item == arr[index]:
            index += 1
        arr[index], item = item, arr[index]

        while index != cur:
            index = cur
            for i in range(cur + 1, len_arr):
                if arr[i] < item:
                    index += 1

            while item == arr[index]:
                index += 1
            arr[index], item = item, arr[index]
            return arr

        return arr
