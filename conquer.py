import random

# Set seed untuk memastikan konsistensi data random
random.seed(40)

# Generate 50 random integers dari 0 hingga 100
data = [random.randint(0, 100) for _ in range(50)]

# Acak data agar tidak terurut
random.shuffle(data)

# Pastikan data benar-benar acak dengan memeriksa output
print("Original Data (Unsorted):", data)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
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

    return arr

# Sorting data menggunakan Merge Sort
sorted_data = merge_sort(data)
print("Sorted Data (Merge Sort):", sorted_data)
