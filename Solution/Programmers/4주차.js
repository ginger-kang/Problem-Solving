function solution(table, languages, preference) {
  let result = [0, ""];
  table.forEach(x => {
    const row = x.split(" ");
    let score = 0;
    row.forEach((language, i) => {
      if (languages.includes(language)) {
        const idx = languages.indexOf(language);
        score += preference[idx] * (6 - i);
      }
    });
    if (result[0] < score) {
      result = [score, row[0]];
    } else if (result[0] === score) {
      const tmp = [result[1], row[0]];
      tmp.sort();

      result = [score, tmp[0]];
    }
  });

  return result[1];
}
