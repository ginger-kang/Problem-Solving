const result = {
  0: 6,
  1: 6,
  2: 5,
  3: 4,
  4: 3,
  5: 2,
  6: 1,
};

function countZero(lottos) {
  const zero = lottos.filter(lotto => lotto === 0);

  return zero.length;
}

function solution(lottos, win_nums) {
  let count = 0;
  let ans = [0, 0];

  const zero = countZero(lottos);
  for (let lotto of lottos) {
    if (win_nums.includes(lotto)) {
      count++;
    }
  }

  ans[0] = result[count + zero];
  ans[1] = result[count];

  return ans;
}
