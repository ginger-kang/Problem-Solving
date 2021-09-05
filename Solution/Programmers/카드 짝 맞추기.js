const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

function getPermutations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map(value => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = getPermutations(rest, selectNumber - 1);
    const attached = permutations.map(permutation => [fixed, ...permutation]);
    results.push(...attached);
  });

  return results;
}

function bfs(board, start) {
  let q = [];
  let visited = Array.from(Array(4), () => Array(4).fill(false));
  let dist = Array.from(Array(4), () => Array(4).fill(0));
  visited[start[0]][start[1]] = true;
  q.push(start);
  while (q.length) {
    const curr = q.shift();
    for (let i = 0; i < 4; i++) {
      let ctrl = 1;
      while (true) {
        const nx = curr[1] + dx[i] * ctrl;
        const ny = curr[0] + dy[i] * ctrl;

        if (nx < 0 || nx >= 4 || ny < 0 || ny >= 4) {
          ctrl -= 1;
          break;
        }
        if (board[ny][nx]) break;

        ctrl += 1;
      }

      for (const j of [1, ctrl]) {
        const nx = curr[1] + dx[i] * j;
        const ny = curr[0] + dy[i] * j;

        if (nx < 0 || nx >= 4 || ny < 0 || ny >= 4 || visited[ny][nx]) continue;
        dist[ny][nx] = dist[curr[0]][curr[1]] + 1;
        visited[ny][nx] = true;
        q.push([ny, nx]);
      }
    }
  }

  return dist;
}

function solution(board, r, c) {
  const cardList = {};
  let cardNumbers = [];
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      if (board[i][j] === 0) continue;
      if (board[i][j] in cardList) {
        cardList[board[i][j]].push([i, j]);
      } else {
        cardList[board[i][j]] = [[i, j]];
      }

      cardNumbers.push(board[i][j]);
    }
  }
  cardNumbers = [...new Set(cardNumbers)].sort();

  let ans = Number.POSITIVE_INFINITY;
  const cardSequence = getPermutations(cardNumbers, cardNumbers.length);
  for (const seq of cardSequence) {
    let result = 0;
    let currPos = [r, c];
    const boardCopy = JSON.parse(JSON.stringify(board));
    for (const targetCard of seq) {
      let tmp = [0, 0];
      for (let i = 0; i < 2; i++) {
        let dist = bfs(boardCopy, currPos);
        tmp[i] = dist[cardList[targetCard][i][0]][cardList[targetCard][i][1]];
      }
      for (let i = 0; i < 2; i++) {
        currPos = cardList[targetCard][i];
        let dist = bfs(boardCopy, currPos);
        tmp[i] +=
          dist[cardList[targetCard][(i + 1) % 2][0]][
            cardList[targetCard][(i + 1) % 2][1]
          ];
      }
      if (tmp[0] < tmp[1]) {
        currPos = cardList[targetCard][1];
        result += tmp[0] + 2;
      } else {
        currPos = cardList[targetCard][0];
        result += tmp[1] + 2;
      }
      const card1 = cardList[targetCard][0];
      const card2 = cardList[targetCard][1];

      boardCopy[card1[0]][card1[1]] = 0;
      boardCopy[card2[0]][card2[1]] = 0;
    }
    ans = Math.min(ans, result);
  }

  return ans;
}
