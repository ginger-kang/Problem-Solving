function bfs(edges, visited, start, n) {
  let queue = [start];
  let dist = new Array(n + 1).fill(-1);
  dist[start] = 0;
  dist[0] = 0;
  visited[start] = true;
  while (queue.length) {
    let now = queue.shift();
    const cost = dist[now] + 1;
    for (let edge of edges) {
      const a = edge[0];
      const b = edge[1];

      if (a == now && visited[b] == false) {
        dist[b] = cost;
        queue.push(b);
        visited[b] = true;
      } else if (b == now && visited[a] == false) {
        dist[a] = cost;
        queue.push(a);
        visited[a] = true;
      }
    }
  }

  const maxVal = Math.max(...dist);
  let ans = dist.filter(x => x === maxVal).length;

  return ans;
}

function solution(n, edge) {
  let visited = new Array(n + 1).fill(false);

  return bfs(edge, visited, 1, n);
}
