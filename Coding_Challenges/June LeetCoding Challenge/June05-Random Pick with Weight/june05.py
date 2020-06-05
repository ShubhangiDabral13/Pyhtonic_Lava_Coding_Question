class Solution:

    def __init__(self, w: List[int]):

        self.prefix_sum = []
        prefix_sum = 0
        for i in w:
            prefix_sum += i
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum


    def pickIndex(self) -> int:

        number = self.total_sum*random.random()
        small, large = 0 , len(self.prefix_sum)
        while small < large :
            medium = small + (large - small)//2
            if number > self.prefix_sum[medium]:
                small = medium + 1
            else:
                large = medium

        return small
