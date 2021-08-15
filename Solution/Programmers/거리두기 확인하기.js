const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function bfs(person, place) {
  const q = [person];
  const visited = Array.from(Array(5), () => Array(5).fill(false));
  let count = 0;
  while (q) {
    let len = q.length;
    while (len--) {
      const [y, x] = q.shift();
      visited[y][x] = true;

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];

        if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5 || visited[ny][nx]) continue;

        if (place[ny][nx] === "X") continue;
        else if (place[ny][nx] === "P") return false;
        else if (place[ny][nx] === "O") q.push([ny, nx]);
      }
    }

    count++;
    if (count === 2 || q === []) return true;
  }

  return true;
}

function solution(places) {
  const ans = [];
  for (let place of places) {
    const people = [];

    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        if (place[i][j] === "P") {
          people.push([i, j]);
        }
      }
    }

    if (!people.length) {
      ans.push(1);
      continue;
    }

    let flag = true;
    for (const person of people) {
      const result = bfs(person, place);
      if (!result) {
        flag = false;
        break;
      }
    }

    if (flag) {
      ans.push(1);
    } else {
      ans.push(0);
    }
  }

  return ans;
}
