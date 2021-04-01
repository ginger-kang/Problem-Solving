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

function solution(infos, queries) {
  let dict = {};
  let result = [];
  for (let info of infos) {
    info = info.split(" ");
    const keys = info.slice(0, 4);
    const score = info.slice(4, 5);
    for (let i = 0; i < 5; i++) {
      const keyList = getCombinations(keys, i);
      if (keyList.length === 0) {
        keyList.push(" ");
        const key = " ";
        if (key in dict) {
          dict[key].push(Number(score));
        } else {
          dict[key] = [Number(score)];
        }
      } else {
        for (let k of keyList) {
          const key = k.join("");
          if (key in dict) {
            dict[key].push(Number(score));
          } else {
            dict[key] = [Number(score)];
          }
        }
      }
    }
  }

  for (let [key, value] of Object.entries(dict)) {
    const sortedValue = value.sort((a, b) => a - b);
    dict[key] = sortedValue;
  }

  for (let query of queries) {
    query = query.replace(/ and/g, "").replace(/\-/g, "").split(" ");
    let key = query.slice(0, 4);
    const score = Number(query.slice(4, 5));

    key = key.join("") === "" ? " " : key.join("");
    if (key in dict) {
      const values = dict[key];
      let left = 0;
      let right = values.length;
      let temp = 0;
      while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (values[mid] >= score) {
          right = mid;
          temp = mid;
        } else {
          left = mid + 1;
        }
      }
      result.push(values.length - temp);
    } else {
      result.push(0);
    }
  }
  return result;
}
