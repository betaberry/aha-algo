def quick_sort(num_list):
    quick_sort_range(num_list, 0 , len(num_list)-1)


def quick_sort_range(num_list, i, j):
    if i >= j:
        return

    pivot = num_list[i]

    left = i + 1
    right = j

    while left <= right:
        # print(f'{left} - {right}')
        if num_list[left] > pivot > num_list[right]:
            swap(num_list, left, right)
        if num_list[left] <= pivot:
            left += 1
        if num_list[right] >= pivot:
            right -= 1
    swap(num_list, i, right)

    quick_sort_range(num_list, i, right - 1)
    quick_sort_range(num_list, right + 1, j)


def swap(num_list, i, j):
    tmp = num_list[i]
    num_list[i] = num_list[j]
    num_list[j] = tmp


if __name__ == '__main__':
    input = [1, 7, 4, 9, 3, 5, 7, 9, 3]
    quick_sort(input)
    print(input)
