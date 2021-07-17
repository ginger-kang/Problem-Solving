class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ['' for _ in range(numRows)]
        row = 0
        flag = 1
        if numRows == 1:
            return s
        for c in s:
            if flag:
                if row == numRows - 1:
                    result[row] += c
                    flag = 0
                    row -= 1
                else:
                    result[row] += c
                    row += 1
            else:
                if row == 0:
                    result[row] += c
                    flag = 1
                    row += 1
                else:
                    result[row] += c
                    row -= 1
        return ''.join(result)