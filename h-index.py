
#Detailed video explanation: https://youtu.be/zzTUtpBQh4k

from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n, i = len(citations), 1
        while i <= n:
            if citations[n - i] < i: break
            i += 1
        return i - 1


citations = [3,0,6,1,5]
s = Solution()
print(s.hIndex(citations))
