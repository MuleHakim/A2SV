class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street) 
        s = [x for x in street]
        count = 0 
        for i in range(n):
            if s[i] == 'H':
                if (i == n-1 and s[i-1] == 'H') or (i == 0 and s[i+1] == 'H'):
                    return -1
                if i < n-1 and s[i+1] == '.':
                    if i != 0 and s[i-1] == 'B':
                        continue
                    s[i+1] = 'B'   
                    count += 1
            
                else:
                    if s[i-1] == 'H':
                        return -1
                    elif s[i-1] != 'B':
                        s[i-1] = 'B'
                        count += 1
        return count 