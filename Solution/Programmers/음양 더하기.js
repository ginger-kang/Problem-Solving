function solution(absolutes, signs) {
  return absolutes.reduce((acc, curr, idx) => {
    if (signs[idx]) {
      return acc + curr;
    } else {
      return acc - curr;
    }
  }, 0);
}
