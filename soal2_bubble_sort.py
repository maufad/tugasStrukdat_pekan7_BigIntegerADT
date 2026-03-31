"""
Soal 2 - Bubble Sort dengan Analisis Langkah
- Early termination
- Mengembalikan tuple (sorted_list, comparisons, swaps, passes)
- Mencetak state array setelah setiap pass
"""

def bubble_sort_with_analysis(arr):
    """
    Bubble sort dengan analisis langkah
    Returns: (sorted_list, total_comparisons, total_swaps, passes_used)
    """
    n = len(arr)
    total_comparisons = 0
    total_swaps = 0
    passes_used = 0
    
    # Salin array agar tidak mengubah array asli
    sorted_list = arr.copy()
    
    print(f"\nArray awal: {sorted_list}")
    print("-" * 40)
    
    for i in range(n - 1):
        swapped = False
        passes_used += 1
        
        # Bandingkan elemen berpasangan
        for j in range(n - 1 - i):
            total_comparisons += 1
            
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                total_swaps += 1
                swapped = True
        
        # Cetak state setelah pass
        print(f"Pass {passes_used}: {sorted_list} (comparisons: {total_comparisons}, swaps: {total_swaps})")
        
        # Early termination: jika tidak ada swap, array sudah terurut
        if not swapped:
            print(f"\n>>> Early termination: tidak ada swap di pass {passes_used}")
            break
    
    return (sorted_list, total_comparisons, total_swaps, passes_used)


# Testing
if __name__ == "__main__":
    print("=" * 50)
    print("Soal 2 - Bubble Sort dengan Analisis")
    print("=" * 50)
    
    # Kasus 1: Array acak
    print("\n[KASUS 1] Array [5, 1, 4, 2, 8]")
    result1 = bubble_sort_with_analysis([5, 1, 4, 2, 8])
    print(f"\nHasil: sorted={result1[0]}, comparisons={result1[1]}, swaps={result1[2]}, passes={result1[3]}")
    
    # Kasus 2: Array sudah terurut
    print("\n[KASUS 2] Array [1, 2, 3, 4, 5]")
    result2 = bubble_sort_with_analysis([1, 2, 3, 4, 5])
    print(f"\nHasil: sorted={result2[0]}, comparisons={result2[1]}, swaps={result2[2]}, passes={result2[3]}")
    
    # Penjelasan
    print("\n" + "=" * 50)
    print("PENJELASAN:")
    print("=" * 50)
    print("""
    Mengapa jumlah pass berbeda?
    
    Kasus 1 [5,1,4,2,8] -> 3 pass:
    - Array belum terurut, masih terjadi pertukaran di setiap pass
    - Pass 1: elemen 8 'mengapung' ke posisi benar
    - Pass 2: elemen 5 ke posisi benar
    - Pass 3: tidak ada swap, program berhenti
    
    Kasus 2 [1,2,3,4,5] -> 1 pass:
    - Array sudah terurut dari awal
    - Pass 1: tidak ada satu pun pertukaran (swapped = False)
    - Early termination aktif, loop berhenti setelah pass 1
    
    Kesimpulan: Early termination membuat bubble sort lebih efisien
    untuk data yang sudah (hampir) terurut.
    """)
