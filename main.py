merged_meeting_ranges = [(3, 5), (0, 1), (4, 8), (10, 12), (9, 10)]

def merge_sorted_arrays(arr1, arr2):
    min_arr, max_arr = (arr1, arr2) if len(arr1) < len(arr2) else (arr2, arr1)
    min_length = len(min_arr)
    max_length = len(max_arr)
    merged_array = []
    min_index, max_index = 0, 0
    while min_index < min_length and max_index < max_length:
        if min_arr[min_index] < max_arr[max_index]:
            merged_array.append(min_arr[min_index])
            min_index += 1
        else:
            merged_array.append(max_arr[max_index])
            max_index += 1
    if min_index == min_length:
        merged_array += max_arr[max_index:]
    else:
        merged_array += min_arr[min_index:]
    return merged_array

def merge_sort(list):
    if len(list) <= 1:
        return list
    return merge_sorted_arrays(merge_sort(list[:len(list) // 2]),
                               merge_sort(list[len(list) // 2:]))

print(merged_meeting_ranges)
sorted_ranges = merge_sort(merged_meeting_ranges)

def merge_ranges():
    if len(sorted_ranges) == 0:
        return

    final_ranges = []

    if len(final_ranges) == 0:
        final_ranges.append(sorted_ranges[0])
        sorted_ranges.remove(sorted_ranges[0])

    while sorted_ranges:
        if final_ranges[0] == sorted_ranges[0]:
            sorted_ranges.remove(sorted_ranges[0])
            continue

        if final_ranges[len(final_ranges) - 1][1] >= sorted_ranges[0][0]:
            final_ranges.append((final_ranges[len(final_ranges) - 1][0], sorted_ranges[0][1]))
            sorted_ranges.remove(sorted_ranges[0])
            final_ranges.remove(final_ranges[len(final_ranges) - 2])
        else:
            final_ranges.append(sorted_ranges[0])
            sorted_ranges.remove(sorted_ranges[0])

    return final_ranges

print(sorted_ranges)
merged_meeting_ranges = merge_ranges()
print(merged_meeting_ranges)