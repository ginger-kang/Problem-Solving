const getCombinations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map(value => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map(combination => [fixed, ...combination]);
    results.push(...attached);
  });

  return results;
};

function solution(numbers) {
  const comb = getCombinations(numbers, 2);
  const ans = [];
  for (let c of comb) {
    const sum = c.reduce((acc, curr) => acc + curr);
    ans.push(sum);
  }

  ans.sort((a, b) => a - b);

  return [...new Set(ans)];
}
