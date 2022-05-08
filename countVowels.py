class Solution:
    def countVowels(self, word: str) -> int:
        output = 0
        vowels = ["a","e","i","o","u"]
        for i, c in enumerate(word):
            if c in vowels:
                output += i*(len(word)-i-1) + len(word)
        return output
