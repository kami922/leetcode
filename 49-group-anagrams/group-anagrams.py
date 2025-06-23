class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for string in strs:
            key = "".join(sorted(list(string)))
            if key in anagram_map:
                anagram_map[key].append(string)
            else:
                anagram_map[key] = [string]
        result = []
        for value in anagram_map.values():
            result.append(value)
        return result





