# Data yang diberikan
data = [1, 5, 6, 4, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Variabel global untuk menghitung operasi
merge_comparisons = 0
quick_comparisons = 0

# Merge Sort
def merge_sort(arr):
    global merge_comparisons
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            merge_comparisons += 1  # Hitung pembandingan
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Quick Sort
def quick_sort(arr):
    global quick_comparisons
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for x in arr[1:]:
            quick_comparisons += 1  # Hitung pembandingan
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Analisis dan Penjelasan
def print_analysis(algorithm_name, comparisons, sorted_data):
    print(f"\n=== Analisis untuk {algorithm_name} ===")
    print(f"Data asli: {data}")
    print(f"Data setelah diurutkan: {sorted_data}")
    print(f"Jumlah operasi pembandingan: {comparisons}")

    if algorithm_name == "Merge Sort":
        print("\n1. Best Case:")
        print("   - Terjadi pada data apapun karena Merge Sort membagi array tanpa memperhatikan urutan data.")
        print("   - Kompleksitas tetap O(n log n).")
        print("\n2. Worst Case:")
        print("   - Sama seperti best case karena pembagian array selalu dilakukan.")
        print("   - Kompleksitas tetap O(n log n).")
        print("\n3. Average Case:")
        print("   - Terjadi pada data rata-rata (acak). Kompleksitas tetap O(n log n).")
    elif algorithm_name == "Quick Sort":
        print("\n1. Best Case:")
        print("   - Terjadi jika pivot selalu memisahkan array secara merata.")
        print("   - Untuk data ini, pembagian cukup baik, sehingga mendekati O(n log n).")
        print("\n2. Worst Case:")
        print("   - Terjadi jika pivot adalah elemen terkecil/terbesar.")
        print("   - Tidak terjadi pada data ini karena pivot tidak selalu ekstrem.")
        print("\n3. Average Case:")
        print("   - Untuk data acak seperti ini, Quick Sort bekerja dengan kompleksitas O(n log n).")

# Eksekusi dan Analisis
print("=== Mulai Pengurutan ===")
# Merge Sort
sorted_data_merge = merge_sort(data.copy())
print_analysis("Merge Sort", merge_comparisons, sorted_data_merge)

# Quick Sort
sorted_data_quick = quick_sort(data.copy())
print_analysis("Quick Sort", quick_comparisons, sorted_data_quick)
