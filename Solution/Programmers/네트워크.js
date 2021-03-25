function dfs(n, v, visited, computers) {
  visited[v] = true;
  for (let i = 0; i < n; i++) {
    if (visited[i] === false && computers[v][i] === 1) {
      dfs(n, i, visited, computers);
    }
  }
}

function solution(n, computers) {
  let visited = [];
  for (let i = 0; i < n; i++) {
    visited.push(false);
  }
  let cnt = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (computers[i][j] === 1 && !visited[i]) {
        dfs(n, i, visited, computers);
        cnt++;
      }
    }
  }
  return cnt;
}
