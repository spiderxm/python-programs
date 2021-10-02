def binary_search(list, data):
    left = 0
    right = len(list) - 1
    found = False

    while left <= right and not found:
        mid_point = (left + right) // 2
        if list[mid_point] == data:
            found = True
            break
        else:
            if data < list[mid_point]:
                right = mid_point
            else:
                left = mid_point

    return found


a = [4, 12, 32, 32, 55, 67, 225, 97]
a.sort()
print(binary_search(a, 97))
