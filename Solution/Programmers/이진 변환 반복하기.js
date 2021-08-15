function solution(s) {
  let ans = [0, 0];
  while (s !== "1") {
    let prev = s.length;
    s = s.split("").filter(c => c === "1");
    let next = s.length;
    let zeroCount = prev - next;

    ans[0] += 1;
    ans[1] += zeroCount;
    s = next.toString(2);
  }

  return ans;
}
