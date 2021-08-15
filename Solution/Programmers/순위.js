function solution(n, results) {
  const graph = Array.from(Array(n + 1), () => Array(n + 1).fill(false));
  results.map(result => {
    const [a, b] = result;
    graph[a][b] = 1;
    graph[b][a] = -1;
    graph[a][a] = 0;
    graph[b][b] = 0;
  });

  const range = [...Array(n).keys()].map(e => e + 1);

  for (const mid of range) {
    for (const a of range) {
      for (const b of range) {
        // a가 mid를 이기고, mid가 b를 이기면 a가 b를 이긴 것과 같음
        if (graph[a][mid] === 1 && graph[mid][b] === 1) graph[a][b] = 1;
        if (graph[a][mid] === -1 && graph[mid][b] === -1) graph[a][b] = -1;
      }
    }
  }

  let ans = 0;
  for (const i of range) {
    let flag = true;
    for (const j of range) {
      if (graph[i][j] === false) {
        flag = false;
        break;
      }
    }
    if (flag) ans++;
  }

  return ans;
}
