import random

# Set seed untuk memastikan konsistensi data random
random.seed(40)

# Generate 50 random integers dari 0 hingga 100
data = [random.randint(0, 100) for _ in range(50)]

# Acak data agar tidak terurut
random.shuffle(data)

# Pastikan data benar-benar acak dengan memeriksa output
print("Original Data (Unsorted):", data)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar posisi elemen jika urutannya salah
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Sorting data menggunakan Bubble Sort
sorted_data = bubble_sort(data)
print("Sorted Data (Bubble Sort):", sorted_data)
