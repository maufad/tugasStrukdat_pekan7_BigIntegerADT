"""
Big Integer ADT - Implementasi dengan Singly Linked List
Setiap digit disimpan dalam satu node, urutan LSB first
"""

class Node:
    """Node untuk menyimpan satu digit"""
    def __init__(self, digit):
        self.digit = digit  # nilai digit (0-9)
        self.next = None    # pointer ke node berikutnya


class BigIntegerLinkedList:
    """Big Integer ADT menggunakan Singly Linked List"""
    
    def __init__(self, init_value="0"):
        """Membuat big integer dari string"""
        self.head = None
        self.is_negative = False
        
        # Handle tanda negatif
        if init_value.startswith('-'):
            self.is_negative = True
            init_value = init_value[1:]
        
        # Simpan digit dari LSB ke MSB (urutan terbalik dari string)
        for ch in reversed(init_value):
            if ch.isdigit():
                self._add_digit_front(int(ch))
        
        self._remove_leading_zeros()
    
    def _add_digit_front(self, digit):
        """Menambah digit di awal linked list (MSB)"""
        new_node = Node(digit)
        new_node.next = self.head
        self.head = new_node
    
    def _add_digit_back(self, digit):
        """Menambah digit di akhir linked list (LSB)"""
        new_node = Node(digit)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def _remove_leading_zeros(self):
        """Hapus digit 0 di awal (MSB)"""
        while self.head and self.head.next and self.head.digit == 0:
            self.head = self.head.next
        if self.head and self.head.digit == 0 and self.head.next is None:
            self.is_negative = False
    
    def to_string(self):
        """Mengembalikan representasi string"""
        if self.head is None:
            return "0"
        
        # Kumpulkan digit dari MSB ke LSB (balik urutan)
        digits = []
        current = self.head
        while current:
            digits.append(str(current.digit))
            current = current.next
        
        # Balik karena kita simpan LSB first
        num_str = ''.join(reversed(digits))
        
        # Hapus leading zeros
        num_str = num_str.lstrip('0')
        if not num_str:
            num_str = "0"
        
        # Tambahkan tanda negatif
        if self.is_negative and num_str != "0":
            num_str = "-" + num_str
        
        return num_str
    
    def __str__(self):
        return self.to_string()
    
    def _get_length(self):
        """Menghitung jumlah digit"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def _to_array(self):
        """Mengembalikan array digit dari MSB ke LSB"""
        digits = []
        current = self.head
        while current:
            digits.append(current.digit)
            current = current.next
        return list(reversed(digits))
    
    def compare(self, other):
        """
        Membandingkan dua big integer
        Return: -1 if self < other, 0 if equal, 1 if self > other
        """
        # Bandingkan tanda
        if self.is_negative != other.is_negative:
            return -1 if self.is_negative else 1
        
        # Sama-sama positif atau sama-sama negatif
        len_self = self._get_length()
        len_other = other._get_length()
        
        if len_self != len_other:
            if self.is_negative:
                return -1 if len_self > len_other else 1
            else:
                return 1 if len_self > len_other else -1
        
        # Bandingkan digit dari MSB
        digits_self = self._to_array()
        digits_other = other._to_array()
        
        for i in range(len(digits_self)):
            if digits_self[i] != digits_other[i]:
                if self.is_negative:
                    return -1 if digits_self[i] > digits_other[i] else 1
                else:
                    return 1 if digits_self[i] > digits_other[i] else -1
        
        return 0
    
    def __eq__(self, other):
        return self.compare(other) == 0
    
    def __ne__(self, other):
        return self.compare(other) != 0
    
    def __lt__(self, other):
        return self.compare(other) < 0
    
    def __le__(self, other):
        return self.compare(other) <= 0
    
    def __gt__(self, other):
        return self.compare(other) > 0
    
    def __ge__(self, other):
        return self.compare(other) >= 0
    
    def add(self, other):
        """Menjumlahkan dua big integer"""
        if self.is_negative == other.is_negative:
            result = BigIntegerLinkedList()
            result.head = self._add_absolute(other)
            result.is_negative = self.is_negative
            result._remove_leading_zeros()
            return result
        else:
            abs_self = self._copy()
            abs_self.is_negative = False
            abs_other = other._copy()
            abs_other.is_negative = False
            
            cmp = abs_self.compare(abs_other)
            if cmp == 0:
                return BigIntegerLinkedList("0")
            
            result = BigIntegerLinkedList()
            if cmp > 0:
                result.head = self._subtract_absolute(abs_other)
                result.is_negative = self.is_negative
            else:
                result.head = abs_other._subtract_absolute(abs_self)
                result.is_negative = other.is_negative
            
            result._remove_leading_zeros()
            return result
    
    def _add_absolute(self, other):
        """Menjumlahkan nilai absolut (kedua positif)"""
        carry = 0
        result_head = None
        tail = None
        
        p = self.head
        q = other.head
        
        while p or q or carry:
            digit_sum = carry
            if p:
                digit_sum += p.digit
                p = p.next
            if q:
                digit_sum += q.digit
                q = q.next
            
            carry = digit_sum // 10
            digit = digit_sum % 10
            
            new_node = Node(digit)
            if result_head is None:
                result_head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
        
        return result_head
    
    def _subtract_absolute(self, other):
        """Mengurangkan nilai absolut (self > other, positif)"""
        borrow = 0
        result_head = None
        tail = None
        
        p = self.head
        q = other.head
        
        while p:
            digit_diff = p.digit - borrow
            if q:
                digit_diff -= q.digit
                q = q.next
            
            if digit_diff < 0:
                digit_diff += 10
                borrow = 1
            else:
                borrow = 0
            
            new_node = Node(digit_diff)
            if result_head is None:
                result_head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            
            p = p.next
        
        return result_head
    
    def subtract(self, other):
        """Mengurangkan other dari self"""
        neg_other = other._copy()
        neg_other.is_negative = not other.is_negative
        return self.add(neg_other)
    
    def _copy(self):
        """Membuat salinan big integer"""
        new_big = BigIntegerLinkedList()
        if self.head is None:
            return new_big
        
        new_big.is_negative = self.is_negative
        new_head = None
        tail = None
        
        current = self.head
        while current:
            new_node = Node(current.digit)
            if new_head is None:
                new_head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            current = current.next
        
        new_big.head = new_head
        return new_big


# Testing
if __name__ == "__main__":
    print("=" * 60)
    print("Big Integer ADT - Singly Linked List Version")
    print("=" * 60)
    
    # Test 1: Constructor dan toString
    num1 = BigIntegerLinkedList("45839")
    print(f"Bilangan 1: {num1.to_string()}")
    
    # Test 2: Penjumlahan
    num2 = BigIntegerLinkedList("12345")
    print(f"Bilangan 2: {num2.to_string()}")
    hasil = num1.add(num2)
    print(f"{num1} + {num2} = {hasil}")
    
    # Test 3: Pengurangan
    num3 = BigIntegerLinkedList("100")
    num4 = BigIntegerLinkedList("1")
    hasil2 = num3.subtract(num4)
    print(f"100 - 1 = {hasil2}")
    
    # Test 4: Bilangan besar
    besar1 = BigIntegerLinkedList("99999999999999999999")
    besar2 = BigIntegerLinkedList("1")
    hasil_besar = besar1.add(besar2)
    print(f"999...999 + 1 = {hasil_besar}")
    
    # Test 5: Bilangan negatif
    neg1 = BigIntegerLinkedList("-100")
    neg2 = BigIntegerLinkedList("50")
    hasil_neg = neg1.add(neg2)
    print(f"-100 + 50 = {hasil_neg}")
    
    # Test 6: Perbandingan
    a = BigIntegerLinkedList("500")
    b = BigIntegerLinkedList("500")
    c = BigIntegerLinkedList("501")
    print(f"500 == 500? {a == b}")
    print(f"500 < 501? {a < c}")
    print(f"500 > 501? {a > c}")
