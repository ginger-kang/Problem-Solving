// 동 남 북 서
const dx = [1, 0, 0, -1];
const dy = [0, 1, -1, 0];

function bfs(n, board, distance) {
  let q = [];
  q.push([0, 0, 0, 0]);
  q.push([0, 0, 0, 1]);
  distance[0][0] = 0;
  while (q.length) {
    const [curr_cost, y, x, direction] = q.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      const next_cost = direction === i ? curr_cost + 100 : curr_cost + 600;

      if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[ny][nx] === 1)
        continue;
      if (distance[ny][nx] === -1 || next_cost <= distance[ny][nx]) {
        distance[ny][nx] = next_cost;
        q.push([next_cost, ny, nx, i]);
      }
    }
  }
}

function solution(board) {
  const n = board.length;
  const distance = Array.from(Array(n), () => Array(n).fill(-1));

  bfs(n, board, distance);

  return distance[n - 1][n - 1];
}
