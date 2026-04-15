import random
import time
import statistics
import matplotlib.pyplot as plt
import argparse

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_location = i
        for j in range(len(arr) - 1 - i):
            if arr[j + i + 1] < arr[min_location]:
                min_location = j + i + 1
        temp = arr[i]
        arr[i] = arr[min_location]
        arr[min_location] = temp

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    return i + 1
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def get_sort_function(algorithm_id):
    if algorithm_id == 1:
        return bubble_sort
    elif algorithm_id == 2:
        return selection_sort
    elif algorithm_id == 3:
        return insertion_sort
    elif algorithm_id == 4:
        return merge_sort
    elif algorithm_id == 5:
        return quick_sort
    else:
        print("invalid algorithm id")
        return None

def generate_random_array(arr_size):
    arr = []
    for i in range(arr_size):
        arr.append(random.randint(0,10000))
    return arr

def measure_running_time(sort_function, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    sort_function(arr_copy)
    end = time.perf_counter()
    return end - start

def plot_avg_runtime_and_std_rand(sort_1,sort_2,sort_3,arr_sizes,rep):
    avg_runtime_1 = []  # first element is for 100 second for 500 ....
    avg_runtime_2 = []
    avg_runtime_3 = []
    std_1 = []  # first element is for 100 second for 500 ....
    std_2 = []
    std_3 = []
    for size in arr_sizes:
        runtime_1 = []
        runtime_2 = []
        runtime_3 = []
        for i in range(rep):
            rand_arr = generate_random_array(size)
            runtime_1.append(measure_running_time(sort_1, rand_arr))
            runtime_2.append(measure_running_time(sort_2, rand_arr))
            runtime_3.append(measure_running_time(sort_3, rand_arr))
        avg_runtime_1.append(statistics.mean(runtime_1))
        std_1.append(statistics.stdev(runtime_1))
        avg_runtime_2.append(statistics.mean(runtime_2))
        std_2.append(statistics.stdev(runtime_2))
        avg_runtime_3.append(statistics.mean(runtime_3))
        std_3.append(statistics.stdev(runtime_3))
    plt.figure(figsize=(10, 6))
    plt.plot(arr_sizes, avg_runtime_1, marker='o', label=sort_1.__name__)
    plt.plot(arr_sizes, avg_runtime_2, marker='o', label=sort_2.__name__)
    plt.plot(arr_sizes, avg_runtime_3, marker='o', label=sort_3.__name__)
    plt.fill_between(arr_sizes, [avg_runtime_1[i] - std_1[i] for i in range(len(arr_sizes))],
        [avg_runtime_1[i] + std_1[i] for i in range(len(arr_sizes))],alpha=0.2)
    plt.fill_between(arr_sizes,
        [avg_runtime_2[i] - std_2[i] for i in range(len(arr_sizes))],
        [avg_runtime_2[i] + std_2[i] for i in range(len(arr_sizes))], alpha=0.2)
    plt.fill_between(arr_sizes,
        [avg_runtime_3[i] - std_3[i] for i in range(len(arr_sizes))],
        [avg_runtime_3[i] + std_3[i] for i in range(len(arr_sizes))], alpha=0.2)
    plt.title("Runtime Comparison (Random Arrays)")
    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("result1.png")
    plt.show()

#------------------------------------part-c------------------------------------------------------------
def generate_sorted_array(arr_size):
    arr = []
    for i in range(arr_size):
        arr.append(random.randint(0, 10000))
    return sorted(arr)
def add_noise(arr, noise_percent):
    arr_copy = arr.copy()
    num_swaps = int(len(arr_copy) * noise_percent / 100)
    for i in range(num_swaps):
        index1 = random.randint(0, len(arr_copy) - 1)
        index2 = random.randint(0, len(arr_copy) - 1)
        temp = arr_copy[index1]
        arr_copy[index1] = arr_copy[index2]
        arr_copy[index2] = temp
    return arr_copy
def plot_avg_runtime_and_std_noise_final(sort_1,sort_2,sort_3,noise,arr_sizes_final,rep):
    avg_runtime_1 = []  # first element is for 100 second for 500 ....
    avg_runtime_2 = []
    avg_runtime_3 = []
    std_1 = []  # first element is for 100 second for 500 ....
    std_2 = []
    std_3 = []
    for size in arr_sizes_final:
        runtime_1 = []
        runtime_2 = []
        runtime_3 = []
        for i in range(rep):
            sorted_arr = generate_sorted_array(size)
            noise_arr = add_noise(sorted_arr,noise)
            runtime_1.append(measure_running_time(sort_1, noise_arr))
            runtime_2.append(measure_running_time(sort_2, noise_arr))
            runtime_3.append(measure_running_time(sort_3, noise_arr))
        avg_runtime_1.append(statistics.mean(runtime_1))
        std_1.append(statistics.stdev(runtime_1))
        avg_runtime_2.append(statistics.mean(runtime_2))
        std_2.append(statistics.stdev(runtime_2))
        avg_runtime_3.append(statistics.mean(runtime_3))
        std_3.append(statistics.stdev(runtime_3))
    plt.figure(figsize=(10, 6))
    plt.plot(arr_sizes_final, avg_runtime_1, marker='o', label=sort_1.__name__)
    plt.plot(arr_sizes_final, avg_runtime_2, marker='o', label=sort_2.__name__)
    plt.plot(arr_sizes_final, avg_runtime_3, marker='o', label=sort_3.__name__)
    plt.fill_between(arr_sizes_final, [avg_runtime_1[i] - std_1[i] for i in range(len(arr_sizes_final))],
        [avg_runtime_1[i] + std_1[i] for i in range(len(arr_sizes_final))],alpha=0.2)
    plt.fill_between(arr_sizes_final,
        [avg_runtime_2[i] - std_2[i] for i in range(len(arr_sizes_final))],
        [avg_runtime_2[i] + std_2[i] for i in range(len(arr_sizes_final))], alpha=0.2)
    plt.fill_between(arr_sizes_final,
        [avg_runtime_3[i] - std_3[i] for i in range(len(arr_sizes_final))],
        [avg_runtime_3[i] + std_3[i] for i in range(len(arr_sizes_final))], alpha=0.2)
    plt.title(f"Runtime Comparison (Nearly Sorted Arrays, noise = {noise}%)")
    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("result2.png")
    plt.show()

#------------------------------------part-d------------------------------------------------------------

if __name__ == "__main__":

    input_reader = argparse.ArgumentParser()
    input_reader.add_argument("-a", nargs=3, type=int, required=True)
    input_reader.add_argument("-s", nargs="+", type=int, required=True)
    input_reader.add_argument("-e", type=int, required=True)
    input_reader.add_argument("-r", type=int, required=True)

    args = input_reader.parse_args()

    sort_1 = get_sort_function(args.a[0])
    sort_2 = get_sort_function(args.a[1])
    sort_3 = get_sort_function(args.a[2])

    if sort_1 is None or sort_2 is None or sort_3 is None:
        quit()

    sizes = args.s
    rep = args.r

    if rep < 2:
        print("number of repetitions must be at least 2")
        quit()

    slow_sorts = [bubble_sort, selection_sort, insertion_sort]
    if sort_1 in slow_sorts or sort_2 in slow_sorts or sort_3 in slow_sorts:
        for size in sizes:
            if size > 10000:
                print("bubble sort, selection sort, and insertion sort are allowed only for sizes up to 10000")
                quit()

    if args.e not in [1, 2]:
        print("invalid experiment type. use 1 for 5% noise or 2 for 20% noise")
        quit()

    # Part B
    plot_avg_runtime_and_std_rand(sort_1, sort_2, sort_3, sizes, rep)

    # Part C
    if args.e == 1:
        plot_avg_runtime_and_std_noise_final(sort_1, sort_2, sort_3, 5, sizes, rep)
    else:
        plot_avg_runtime_and_std_noise_final(sort_1, sort_2, sort_3, 20, sizes, rep)


#------------------------------------------------------------FIN-------------------------------------------------------------------

