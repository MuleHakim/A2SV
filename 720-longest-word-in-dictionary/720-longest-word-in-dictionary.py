class Solution:
    def longestWord(self, words: List[str]) -> str:
        output = ['']
        words = sorted(words,key=len)
        for word in words:
            if word[:-1] in output:
                output.append(word)
        output = sorted(output)
        return max(output,key=len)