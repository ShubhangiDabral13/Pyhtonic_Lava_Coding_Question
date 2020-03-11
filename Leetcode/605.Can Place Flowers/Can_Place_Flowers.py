class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if(len(flowerbed)>=2):
            if(flowerbed[0] == 0 and flowerbed[1] == 0):
                count += 1
                flowerbed[0] = 1
            if(flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0):
                count += 1
                flowerbed[len(flowerbed)-1] = 1
            for i in range(1,len(flowerbed)-1):
                if(flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] ==0):
                    count += 1
                    flowerbed[i] = 1
        else:
            if(flowerbed[0] == 0):
                count += 1

        if (count >= n):
            return True
        else:
            return False      
