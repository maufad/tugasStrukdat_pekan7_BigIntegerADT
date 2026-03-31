"""
Soal 4 - Merge Tiga Sorted Lists
Menggabungkan 3 sorted list dalam satu pass O(n) menggunakan 3 pointer
"""

def merge_three_sorted_lists(listA, listB, listC):
    """
    Menggabungkan 3 sorted list menjadi 1 sorted list dalam O(n)
    Menggunakan 3 pointer dalam satu pass
    """
    result = []
    
    # Pointer untuk masing-masing list
    i = j = k = 0
    
    # Panjang masing-masing list
    lenA, lenB, lenC = len(listA), len(listB), len(listC)
    
    # Proses selama masih ada elemen di minimal 2 list
    while i < lenA or j < lenB or k < lenC:
        # Nilai default (infinity) jika list sudah habis
        valA = listA[i] if i < lenA else float('inf')
        valB = listB[j] if j < lenB else float('inf')
        valC = listC[k] if k < lenC else float('inf')
        
        # Cari nilai minimum
        if valA <= valB and valA <= valC:
            result.append(valA)
            i += 1
        elif valB <= valA and valB <= valC:
            result.append(valB)
            j += 1
        else:
            result.append(valC)
            k += 1
    
    return result


# Versi alternatif dengan logika yang lebih jelas
def merge_three_sorted_lists_v2(listA, listB, listC):
    """Versi dengan while loop terpisah untuk setiap kondisi"""
    result = []
    i = j = k = 0
    lenA, lenB, lenC = len(listA), len(listB), len(listC)
    
    # Selama ketiga list masih punya elemen
    while i < lenA and j < lenB and k < lenC:
        if listA[i] <= listB[j] and listA[i] <= listC[k]:
            result.append(listA[i])
            i += 1
        elif listB[j] <= listA[i] and listB[j] <= listC[k]:
            result.append(listB[j])
            j += 1
        else:
            result.append(listC[k])
            k += 1
    
    # Jika listA dan listB masih ada
    while i < lenA and j < lenB:
        if listA[i] <= listB[j]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listB[j])
            j += 1
    
    # Jika listA dan listC masih ada
    while i < lenA and k < lenC:
        if listA[i] <= listC[k]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listC[k])
            k += 1
    
    # Jika listB dan listC masih ada
    while j < lenB and k < lenC:
        if listB[j] <= listC[k]:
            result.append(listB[j])
            j += 1
        else:
            result.append(listC[k])
            k += 1
    
    # Jika hanya listA yang tersisa
    while i < lenA:
        result.append(listA[i])
        i += 1
    
    # Jika hanya listB yang tersisa
    while j < lenB:
        result.append(listB[j])
        j += 1
    
    # Jika hanya listC yang tersisa
    while k < lenC:
        result.append(listC[k])
        k += 1
    
    return result


# Testing
if __name__ == "__main__":
    print("=" * 50)
    print("Soal 4 - Merge Tiga Sorted Lists")
    print("=" * 50)
    
    # Test case 1
    A = [1, 5, 9]
    B = [2, 6, 10]
    C = [3, 4, 7]
    
    print(f"List A: {A}")
    print(f"List B: {B}")
    print(f"List C: {C}")
    print(f"Hasil merge: {merge_three_sorted_lists(A, B, C)}")
    print(f"Expected: [1, 2, 3, 4, 5, 6, 7, 9, 10]")
    
    print("\n" + "-" * 50)
    
    # Test case 2 - panjang berbeda
    A = [1, 8]
    B = [2, 3, 9]
    C = [4, 5, 6, 7]
    
    print(f"List A: {A}")
    print(f"List B: {B}")
    print(f"List C: {C}")
    print(f"Hasil merge: {merge_three_sorted_lists(A, B, C)}")
    print(f"Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    
    print("\n" + "=" * 50)
    print("ANALISIS KOMPLEKSITAS:")
    print("=" * 50)
    print("""
    Time Complexity: O(n) dimana n = lenA + lenB + lenC
    - Setiap elemen dari ketiga list diproses tepat satu kali
    
    Space Complexity: O(n) untuk menyimpan hasil
    
    Keunggulan dibandingkan merge bertahap:
    - Satu pass, tidak perlu array sementara
    - Lebih efisien secara memori dan konstanta waktu
    """)
