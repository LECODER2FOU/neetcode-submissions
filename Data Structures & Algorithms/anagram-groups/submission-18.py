class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            count=[0] * 26
            for j in range(len(i)):
                count[ord(i[j])-ord('a')] +=1
            key = tuple(count)
            res[key].append(i)
        return list(res.values())