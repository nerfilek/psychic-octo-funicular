import random
import time

# Генерация случайного списка чисел
def generate_random_list(size, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

# Быстрая сортировка (O(n log n))
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Сортировка вставками (O(n^2))
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Пузырьковая сортировка (O(n^2))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Линейный поиск (O(n))
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Бинарный поиск (O(log n))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Функция измерения времени выполнения
def measure_time(func, arr, *args):
    start = time.time()
    result = func(arr, *args) if args else func(arr)
    return result, time.time() - start

# Главная функция
def main():
    size = 100
    random_list = generate_random_list(size, 0, 1000)

    # Сортировка и измерение времени
    sorted_list, quick_time = measure_time(quick_sort, random_list)
    _, insertion_time = measure_time(insertion_sort, random_list.copy())
    _, bubble_time = measure_time(bubble_sort, random_list.copy())

    print(f"Quick Sort Time: {quick_time:.6f} sec")
    print(f"Insertion Sort Time: {insertion_time:.6f} sec")
    print(f"Bubble Sort Time: {bubble_time:.6f} sec")

    # Поиск элемента
    target = random.choice(sorted_list)
    lin_index, lin_time = measure_time(linear_search, sorted_list, target)
    bin_index, bin_time = measure_time(binary_search, sorted_list, target)

    print(f"Linear Search Time: {lin_time:.6f} sec, Found at index: {lin_index}")
    print(f"Binary Search Time: {bin_time:.6f} sec, Found at index: {bin_index}")

if __name__ == "__main__":
    main()