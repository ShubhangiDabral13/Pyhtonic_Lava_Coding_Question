class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        fw = [self.f(s) for s in words]
        fq = [self.f(q) for q in queries]

        result = []
        for q in fq:
            count = 0
            for w in fw:
                if q<w:
                    count += 1
            result.append(count)

        return result
    def f(self,s):
        n = s.count(min(s))
        return n
