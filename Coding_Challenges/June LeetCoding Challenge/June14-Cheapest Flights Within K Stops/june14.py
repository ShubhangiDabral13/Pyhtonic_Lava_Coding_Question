class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        graph = collections.defaultdict(dict)
        for flight in flights:
            graph[flight[0]][flight[1]] = flight[2]
        heap = [(0, src, K+1)]
        while heap:
            dist, node, stops = heappop(heap)
            if node == dst:
                return dist
            if stops > 0:
                for i in graph[node]:
                    heappush(heap, (dist+graph[node][i], i, stops-1))
        return -1


        
