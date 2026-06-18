class Solution:
    def merge(self, iv: List[List[int]]) -> List[List[int]]:
        iv.sort()
        s, e = iv[0][0], iv[0][1]
        i = 0
        res = []
        while i < len(iv) - 1:
            if iv[i+1][0] > e:
                res.append([s, e])
                s = iv[i+1][0]
                e = iv[i+1][1]
            else:
                e = max(e, iv[i+1][1])
            i += 1
        res.append([s, e])
        return res