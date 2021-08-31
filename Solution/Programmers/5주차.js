let cnt = 0;
let ans = 0;

function BT(s, alphas, word) {
  if (s === word) {
    ans = cnt;
    return;
  }
  if (s.length === 5) return;
  for (const alpha of alphas) {
    cnt++;
    s += alpha;
    BT(s, alphas, word);
    s = s.slice(0, s.length - 1);
  }
}

function solution(word) {
  const alphas = ["A", "E", "I", "O", "U"];

  BT("", alphas, word);

  return ans;
}
