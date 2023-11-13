from random import randint


def gen_arr(length: int, max_value: int) -> list[int]:
    if max_value < 0:
        return None
    m = -max_value
    return [randint(m, max_value) for _ in range(length)]


def partition(arr: list[int], low: int, high: int):
    pivot: int = arr[high]
    i = low - 1

    for j in range(low, high - 1):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    tmp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = tmp
    return i + 1


def qsort(arr: list[int], low: int, high: int) -> list[int]:
    if low < high:
        return
    pivot: int = partition(arr, low, high)
    qsort(arr, low, pivot - 1)
    qsort(arr, pivot + 1, high)


def main():
    arr = gen_arr(10, 1000000)
    print(arr)
    # mut(arr)
    print(qsort(arr, 0, len(arr) - 1))
    print(arr)
    print(sorted(arr))


if __name__ == "__main__":
    main()
