class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        len1, len2 = len(word1), len(word2)
        max_length = max(len1, len2)
        
        for i in range(max_length):
            if i < len1:
                result += word1[i]
            if i < len2:
                result += word2[i]
                
        return result

solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"