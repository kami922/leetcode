class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numericals = [
        [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"],
        [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"],
        [5, "V"], [4, "IV"], [1, "I"]
        ]   
        roman = ""
        for i in range(len(roman_numericals)):
            current_int_val = roman_numericals[i][0]
            current_roman_val = roman_numericals[i][1]
            while num >= current_int_val:
                roman += current_roman_val
                num -= current_int_val

        return roman
