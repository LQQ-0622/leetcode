import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = collections.defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            mp[key].append(str)
        return list(mp.values())


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = Solution().groupAnagrams(input)
print(result)
