class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            sum_bits = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)

            result.append(str(sum_bits))

            i -= 1
            j -= 1

        return "".join(result[::-1])