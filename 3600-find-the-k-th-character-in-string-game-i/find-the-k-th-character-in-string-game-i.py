class Solution:
    def kthCharacter(self, k: int) -> str:
        
        def generate_next_string(s):
            """
            Generates the next string by appending the next character for each character in the input string.
            """
            next_str = ""
            for char in s:
                next_char = chr(ord(char) + 1) if char != 'z' else 'a'
                next_str += char + next_char
            return next_str

        word = "a"
        while len(word) < k:
            word = generate_next_string(word)

        return word[k - 1]

        