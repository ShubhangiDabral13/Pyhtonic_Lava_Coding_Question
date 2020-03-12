class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        for i in range(int(area**.5),-1,-1):
            if area%i == 0:
                break
        return [area//i,i]
        
