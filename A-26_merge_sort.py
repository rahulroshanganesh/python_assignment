def merge_sort(arr):
    iterations = 0
    comparisons = 0
    swaps = 0

    def merge(left, right):
        nonlocal comparisons, swaps
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                swaps += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(sub_arr):
        nonlocal iterations
        if len(sub_arr) <= 1:
            return sub_arr

        iterations += 1
        mid = len(sub_arr) // 2
        left = sort(sub_arr[:mid])
        right = sort(sub_arr[mid:])

        return merge(left, right)

    sorted_arr = sort(arr)
    return sorted_arr, iterations, comparisons, swaps

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr, iterations, comparisons, swaps = merge_sort(arr)

print("Sorted array:", sorted_arr)
print("Number of iterations:", iterations)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)
