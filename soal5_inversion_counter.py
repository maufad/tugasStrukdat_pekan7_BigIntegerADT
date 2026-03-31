"""
Soal 5 - Inversions Counter
Menghitung jumlah inversi dalam array
- Naive: O(n²)
- Smart (Merge Sort): O(n log n)
"""

import random
import time

# ============ NAIVE APPROACH (O(n²)) ============
def count_inversions_naive(arr):
    """
    Menghitung inversi dengan brute force O(n²)
    Cek semua pasangan (i, j) dengan i < j
    """
    n = len(arr)
    count = 0
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    
    return count


# ============ SMART APPROACH (O(n log n)) ============
def merge_and_count(arr, temp_arr, left, mid, right):
    """
    Merge dua subarray dan hitung inversi
    Returns jumlah inversi yang terjadi saat merge
    """
    i = left      # Pointer untuk subarray kiri
    j = mid + 1   # Pointer untuk subarray kanan
    k = left      # Pointer untuk array sementara
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # Jika arr[i] > arr[j], maka semua elemen dari i..mid > arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    # Salin sisa elemen dari subarray kiri
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    # Salin sisa elemen dari subarray kanan
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    # Salin kembali ke array asli
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    """
    Merge sort yang menghitung inversi
    Returns jumlah inversi dalam array
    """
    inv_count = 0
    
    if left < right:
        mid = (left + right) // 2
        
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    
    return inv_count


def count_inversions_smart(arr):
    """
    Menghitung inversi menggunakan merge sort O(n log n)
    """
    temp_arr = [0] * len(arr)
    arr_copy = arr.copy()
    return merge_sort_and_count(arr_copy, temp_arr, 0, len(arr) - 1)


# ============ TESTING ============
def test_inversion_counters():
    """Uji kedua fungsi dengan berbagai kasus"""
    test_cases = [
        ([1, 2, 3, 4, 5], 0, "Array terurut"),
        ([5, 4, 3, 2, 1], 10, "Array terbalik"),
        ([2, 3, 8, 6, 1], 5, "Contoh campuran"),
        ([1, 20, 6, 4, 5], 5, "Contoh lain"),
        ([1, 1, 1, 1, 1], 0, "Semua sama"),
        ([3, 1, 2], 2, "Array kecil"),
        ([1], 0, "Satu elemen"),
        ([], 0, "Array kosong")
    ]
    
    print("=" * 70)
    print(f"{'Test Case':<30} {'Naive':<10} {'Smart':<10} {'Sama?':<10}")
    print("=" * 70)
    
    for arr, expected, desc in test_cases:
        if len(arr) == 0:
            naive = 0
            smart = 0
        else:
            naive = count_inversions_naive(arr)
            smart = count_inversions_smart(arr)
        
        sama = "✓" if naive == smart == expected else "✗"
        print(f"{desc:<30} {naive:<10} {smart:<10} {sama:<10}")
    
    print("=" * 70)


# ============ BENCHMARK ============
def benchmark_inversion_counters():
    """Membandingkan waktu eksekusi naive vs smart"""
    sizes = [1000, 5000, 10000]
    
    print("\n" + "=" * 80)
    print("BENCHMARK INVERSION COUNTER")
    print("=" * 80)
    print(f"{'Ukuran (n)':<15} {'Naive (detik)':<20} {'Smart (detik)':<20} {'Percepatan':<15}")
    print("=" * 80)
    
    for size in sizes:
        # Generate array random
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        # Ukur naive
        start = time.time()
        naive_count = count_inversions_naive(arr)
        naive_time = time.time() - start
        
        # Ukur smart
        start = time.time()
        smart_count = count_inversions_smart(arr)
        smart_time = time.time() - start
        
        # Verifikasi hasil sama
        assert naive_count == smart_count, "Hasil berbeda!"
        
        # Hitung percepatan
        speedup = naive_time / smart_time if smart_time > 0 else 0
        
        print(f"{size:<15} {naive_time:<20.6f} {smart_time:<20.6f} {speedup:<15.2f}x")
    
    print("=" * 80)


# ============ MAIN ============
if __name__ == "__main__":
    print("=" * 50)
    print("Soal 5 - Inversions Counter")
    print("=" * 50)
    
    test_inversion_counters()
    benchmark_inversion_counters()
    
    print("\n" + "=" * 50)
    print("PENJELASAN:")
    print("=" * 50)
    print("""
    Mengapa Merge Sort Lebih Cepat?
    
    1. Kompleksitas Algoritma:
       - Naive (Brute Force): O(n²) → n(n-1)/2 operasi
       - Smart (Merge Sort): O(n log n) → ~ n * log₂(n) operasi
    
    2. Perbandingan untuk n = 10.000:
       - Naive: ~50 juta operasi
       - Smart: ~140 ribu operasi (357x lebih cepat!)
    
    3. Cara Kerja Smart:
       - Manfaatkan sifat divide and conquer
       - Saat merge dua subarray terurut, jika L[i] > R[j],
         maka semua elemen L[i..mid] > R[j] → tambah (mid-i+1) inversi
    
    4. Aplikasi Inversion Counter:
       - Mengukur seberapa 'tidak terurut' suatu array
       - Menghitung kemiripan ranking (collaborative filtering)
       - Analisis data dan statistik
    """)
