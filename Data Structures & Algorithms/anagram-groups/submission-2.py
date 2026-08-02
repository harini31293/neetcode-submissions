class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) -ord('a')] +=1
                print(count)
                print(5555)
            print(9999)
            res[tuple(count)].append(s)
        return list(res.values())

        