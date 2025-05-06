class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False  # Negative numbers and zero are not powers of two
        if n == 1:
            return True  # Base case: 2^0 = 1
        if n % 2 != 0:
            return False  # If n is odd, it's not a power of two
        return self.isPowerOfTwo(n // 2)