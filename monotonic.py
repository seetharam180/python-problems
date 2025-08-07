def is_monotonic(arr):
    if not arr:
        return True

    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing
arr=[1,2,3,4,5]
print(is_monotonic(arr))