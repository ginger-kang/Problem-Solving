const getCombinations = function (arr, selectNumber) {
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

function solution(orders, course) {
  const result = [];
  let ans = [];
  for (let num of course) {
    let menu = {};
    for (let order of orders) {
      const orderArr = order.split("").sort((a, b) => a.localeCompare(b));
      const orderComb = getCombinations(orderArr, num);
      for (let od of orderComb) {
        const key = od.join("");
        if (key in menu) {
          menu[key] += 1;
        } else {
          menu[key] = 1;
        }
      }
    }
    const sortedValue = Object.entries(menu);
    sortedValue.sort((a, b) => b[1] - a[1]);
    if (!sortedValue.length) continue;

    const maxVal = sortedValue[0][1];
    for (const value of sortedValue) {
      if (value[1] < maxVal) break;
      if (value[1] >= 2 && value[1] === maxVal) {
        result.push(value[0]);
      }
    }
  }

  return result.sort((a, b) => a.localeCompare(b));
}
