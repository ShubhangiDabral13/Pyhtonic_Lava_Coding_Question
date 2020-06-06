class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ret = [[]]*len(people)
        people.sort(key = lambda x: (x[0],-x[1]))
        indices = [i for i in range(len(people))]
        for j,(_,pk) in enumerate(people):
            i = indices.pop(pk)
            ret[i] = people[j]
        return ret
        
