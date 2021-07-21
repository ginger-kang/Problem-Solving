class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        idx = 1
        result = []
        while S:
            flag = True
            left = S[:idx]
            right = S[idx:]
            #print(left, right)
            for j in left:
                if j in right:
                    flag = False
            if flag:
                S = right
                result.append(len(left))
                idx = 1
            else:
                idx += 1
        return result