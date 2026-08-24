class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []

        for word in strs :
            freq = [0] * 26

            for c in word :
                freq[ord(c) - ord('a')] += 1

            freq_key = tuple(freq)
            
            if freq_key not in map :
                map[freq_key] = [word]
            else :
                map[freq_key].append(word)
        

        for _ , words in map.items() :
            res.append(words)
            
        return res