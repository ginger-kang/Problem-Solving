function solution(operations) {
  const q = [];
  for (let operation of operations) {
    let [cmd, x] = operation.split(" ");
    x *= 1;
    if (cmd === "I") {
      q.push(x);
    } else {
      if (x === 1) {
        const idx = q.indexOf(Math.max(...q));
        q.splice(idx, 1);
      } else {
        const idx = q.indexOf(Math.min(...q));
        q.splice(idx, 1);
      }
    }
  }

  const ans = [0, 0];
  if (!q.length) return [0, 0];
  ans[0] = Math.max(...q);
  ans[1] = Math.min(...q);

  return ans;
}
