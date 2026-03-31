"""
Soal 3 - Hybrid Sort
- Insertion sort untuk sub-array ≤ threshold
- Selection sort untuk sub-array > threshold
- Membandingkan jumlah operasi dengan pure insertion dan selection sort
"""

import random
import time

# ============ PURE INSERTION SORT ============
def insertion_sort_with_ops(arr):
    """Insertion sort yang mengembalikan (sorted_arr, total_operations)"""
    comparisons = 0
    swaps = 0
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        
        if j >= 0:
            comparisons += 1  # Untuk perbandingan yang gagal
        
        arr[j + 1] = key
        if j + 1 != i:
            swaps += 1
    
    return arr, comparisons + swaps


# ============ PURE SELECTION SORT ============
def selection_sort_with_ops(arr):
    """Selection sort yang mengembalikan (sorted_arr, total_operations)"""
    comparisons = 0
    swaps = 0
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return arr, comparisons + swaps


# ============ HYBRID SORT ============
def hybrid_sort_with_ops(arr, threshold=10):
    """
    Hybrid sort: 
    - Insertion sort jika panjang ≤ threshold
    - Selection sort jika panjang > threshold
    """
    arr = arr.copy()
    n = len(arr)
    
    if n <= threshold:
        sorted_arr, ops = insertion_sort_with_ops(arr)
        return sorted_arr, ops
    else:
        sorted_arr, ops = selection_sort_with_ops(arr)
        return sorted_arr, ops


# ============ UTILITY ============
def generate_random_array(size):
    """Membuat array random dengan ukuran tertentu"""
    return [random.randint(1, 1000) for _ in range(size)]


def generate_nearly_sorted_array(size):
    """Membuat array yang hampir terurut (95% terurut)"""
    arr = list(range(size))
    # Acak 5% elemen
    for _ in range(size // 20):
        i, j = random.randint(0, size - 1), random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# ============ EKSPERIMEN ============
def run_experiment():
    """Menjalankan eksperimen perbandingan"""
    sizes = [50, 100, 500]
    
    print("=" * 80)
    print("EKSPERIMEN 1: DATA RANDOM")
    print("=" * 80)
    print(f"{'Ukuran':<10} {'Hybrid Sort':<15} {'Insertion Sort':<18} {'Selection Sort':<15}")
    print("-" * 80)
    
    for size in sizes:
        arr = generate_random_array(size)
        
        _, hybrid_ops = hybrid_sort_with_ops(arr, threshold=10)
        _, insertion_ops = insertion_sort_with_ops(arr)
        _, selection_ops = selection_sort_with_ops(arr)
        
        print(f"{size:<10} {hybrid_ops:<15} {insertion_ops:<18} {selection_ops:<15}")
    
    print("\n" + "=" * 80)
    print("EKSPERIMEN 2: DATA HAMPIR TERURUT (threshold=20)")
    print("=" * 80)
    print(f"{'Ukuran':<10} {'Hybrid Sort':<15} {'Insertion Sort':<18} {'Selection Sort':<15}")
    print("-" * 80)
    
    for size in sizes:
        arr = generate_nearly_sorted_array(size)
        
        _, hybrid_ops = hybrid_sort_with_ops(arr, threshold=20)
        _, insertion_ops = insertion_sort_with_ops(arr)
        _, selection_ops = selection_sort_with_ops(arr)
        
        print(f"{size:<10} {hybrid_ops:<15} {insertion_ops:<18} {selection_ops:<15}")
    
    print("=" * 80)


# ============ MAIN ============
if __name__ == "__main__":
    print("=" * 50)
    print("Soal 3 - Hybrid Sort")
    print("=" * 50)
    run_experiment()
