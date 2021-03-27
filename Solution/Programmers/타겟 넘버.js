let ans = 0;

function dfs(numbers, target, sum, v) {
  if (sum === target && v === numbers.length) {
    ans++;
    return;
  }
  if (v === numbers.length) return;

  dfs(numbers, target, sum + numbers[v], v + 1);
  dfs(numbers, target, sum - numbers[v], v + 1);
}

function solution(numbers, target) {
  dfs(numbers, target, 0, 0);
  return ans;
}
