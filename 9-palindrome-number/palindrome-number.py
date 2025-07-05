class Solution:
    def _check_palindrome_recursive(self, s: str, left: int) -> bool:
        """
        Helper function to recursively check if a string is a palindrome.
        Compares characters from the start and end, moving inwards.
        """
        # Base case 1: If the left pointer has crossed or met the middle,
        # it means all checked characters have matched.
        if left >= len(s) // 2:
            return True

        # Base case 2: If characters at the current left and corresponding right
        # positions do not match, it's not a palindrome.
        if s[left] != s[len(s) - 1 - left]:
            return False

        # Recursive step: Move the left pointer one step to the right
        # and continue checking.
        return self._check_palindrome_recursive(s, left + 1)

    def isPalindrome(self, x: int) -> bool:
        """
        Checks if an integer is a palindrome.
        """
        # As per the C++ logic, first convert the integer to a string.
        # Handle negative numbers: In a typical palindrome definition,
        # negative numbers are not considered palindromes (e.g., -121 is not 121-).
        # The C++ code would convert -121 to "-121" and then fail the palindrome check,
        # which is the common interpretation.
        if x < 0:
            return False # Negative numbers are generally not palindromes

        s = str(x) # Convert integer to string

        # Start the recursive check from the beginning of the string (left pointer at 0)
        return self._check_palindrome_recursive(s, 0)