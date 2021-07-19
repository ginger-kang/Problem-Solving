from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def bfs(image, color):
            q = deque()
            q.append((sr, sc))
            image[sr][sc] = newColor
            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or image[ny][nx] != color:
                        continue
                    image[ny][nx] = newColor
                    q.append((ny ,nx))
        
        n, m, color = len(image), len(image[0]), image[sr][sc]
        if color == newColor:
            return image
        bfs(image, color)
        
        return image