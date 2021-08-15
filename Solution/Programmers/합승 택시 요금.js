function solution(n, s, a, b, fares) {
  const graph = Array.from(Array(n + 1), () => Array(n + 1).fill(Infinity));

  fares.forEach(fare => {
    const [c, d, f] = fare;
    graph[c][d] = f;
    graph[d][c] = f;
  });

  for (let k = 1; k < n + 1; k++) {
    for (let i = 1; i < n + 1; i++) {
      for (let j = 1; j < n + 1; j++) {
        if (i === j) graph[i][j] = 0;
        if (graph[i][k] + graph[k][j] < graph[i][j]) {
          graph[i][j] = graph[i][k] + graph[k][j];
        }
      }
    }
  }

  let ans = graph[s][a] + graph[s][b];
  for (let i = 1; i < n + 1; i++) {
    ans = Math.min(ans, graph[s][i] + graph[i][a] + graph[i][b]);
  }

  return ans;
}
