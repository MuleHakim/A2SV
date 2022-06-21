class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            cnt = 0
            for char in chars[i:]:
                if char != chars[i]:
                    break
                cnt += 1
            if cnt != 1:
                newList = list(str(cnt))
                chars[i+1:i+cnt] = newList
                i += 1 + len(newList)  
            else:
                i += 1
        return len(chars)