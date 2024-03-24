class Solution:
    def intToRoman(self, num: int) -> str:
        values = {'I': 1, 'IV': 4, 'V': 5,'IX': 9, 'X': 10,'XL': 40, 'L': 50, 'XC': 90, 'C': 100,'CD': 400, 'D': 500,'CM': 900, 'M': 1000}
        roman_numeral = ""
        for numeral, value in sorted(values.items(), key=lambda x: x[1], reverse=True):
            while num >= value:
                roman_numeral += numeral
                num -= value
        return roman_numeral

if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(num = 3))        