"""
Soal 1 - Modified Binary Search
Menghitung jumlah kemunculan target dalam sorted list O(log n)
"""

def find_first_occurrence(sorted_list, target):
    """Mencari indeks pertama kemunculan target"""
    left, right = 0, len(sorted_list) - 1
    first_pos = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_list[mid] == target:
            first_pos = mid
            right = mid - 1  # Cari lagi ke kiri
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return first_pos


def find_last_occurrence(sorted_list, target):
    """Mencari indeks terakhir kemunculan target"""
    left, right = 0, len(sorted_list) - 1
    last_pos = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_list[mid] == target:
            last_pos = mid
            left = mid + 1  # Cari lagi ke kanan
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return last_pos


def count_occurrences(sorted_list, target):
    """
    Menghitung berapa kali target muncul dalam sorted list
    Time complexity: O(log n)
    """
    first = find_first_occurrence(sorted_list, target)
    
    if first == -1:
        return 0
    
    last = find_last_occurrence(sorted_list, target)
    return last - first + 1


# Testing
if __name__ == "__main__":
    print("=" * 50)
    print("Soal 1 - Count Occurrences")
    print("=" * 50)
    
    data = [1, 2, 4, 4, 4, 7, 9, 12]
    
    print(f"List: {data}")
    print(f"countOccurrences(4) → {count_occurrences(data, 4)}")  # Output: 3
    print(f"countOccurrences(5) → {count_occurrences(data, 5)}")  # Output: 0
    print(f"countOccurrences(1) → {count_occurrences(data, 1)}")  # Output: 1
    print(f"countOccurrences(12) → {count_occurrences(data, 12)}")  # Output: 1
