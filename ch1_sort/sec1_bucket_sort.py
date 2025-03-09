def bucket_sort(obj_list: list):
    if obj_list is None or len(obj_list) == 0:
        return
    _min = obj_list[0]
    _max = obj_list[0]
    for obj in obj_list:
        if obj < _min:
            _min = obj
        elif obj > _max:
            _max = obj

    bucket = [0 for i in range(_min, _max + 1)]

    for obj in obj_list:
        bucket[obj - _min] += 1

    for i, b in enumerate(bucket):
        while b > 0:
            print(f'{i + _min} ', end='')
            b -= 1


if __name__ == '__main__':
    input = [1, 7, 4, 9, 3, 5, 7, 9, 3]
    bucket_sort(input)
