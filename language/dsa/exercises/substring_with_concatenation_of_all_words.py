from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        output = []
        word_counts = {}

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        word_length = len(words[0])
        window_size = word_length * len(words)

        start_index = 0
        end_index = window_size - 1

        while end_index < len(s):
            tmp_word_counts = {}
            current_start = start_index
            current_end = start_index + word_length - 1

            while current_end <= end_index:
                current_word = s[current_start:current_end + 1]
                if current_word in tmp_word_counts:
                    tmp_word_counts[current_word] += 1
                else: 
                    tmp_word_counts[current_word] = 1
                current_start = current_end + 1
                current_end = current_end + word_length

            if tmp_word_counts == word_counts:
                output.append(start_index)

            start_index += 1
            end_index += 1

        return output
    
solution = Solution()
print(solution.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
