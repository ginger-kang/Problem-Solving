class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(word):
            patternDict = {}
            pattern = 'a'
            patternDict[word[0]] = ord('a')
            prev = ord('a')
            for c in range(1, len(word)):
                if word[c] in patternDict:
                    pattern += chr(patternDict[word[c]])
                else:
                    patternDict[word[c]] = prev + 1
                    pattern += chr(prev + 1)
                    prev += 1
                # print(pattern)
                
            return pattern
        
        patternConvert = convert(pattern)
        
        result = []
        for word in words:
            result.append([word, convert(word)])
        
        ans = []
        for word, pattern in result:
            if pattern == patternConvert:
                ans.append(word)
        
        return ans
        