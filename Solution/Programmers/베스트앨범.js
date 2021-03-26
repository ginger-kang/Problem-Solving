const comp = (a, b) => {
  const aSum = a[1].reduce((a, c) => {
    return a + c[0];
  }, 0);
  const bSum = b[1].reduce((a, c) => {
    return a + c[0];
  }, 0);
  return bSum - aSum;
};

function solution(genres, plays) {
  let tempAlbum = new Map();
  let ans = [];
  genres.forEach((genre, index) => {
    const tmp = tempAlbum.get(genre);
    if (tmp) {
      tempAlbum.set(genre, [...tmp, [plays[index], index]]);
    } else {
      tempAlbum.set(genre, [[plays[index], index]]);
    }
  });
  const album = new Map([...tempAlbum.entries()].sort((a, b) => comp(a, b)));
  for (let [key, value] of album.entries()) {
    album.set(
      key,
      album.get(key).sort((a, b) => b[0] - a[0]),
    );
  }
  let cnt = 0;
  for (let [key, value] of album) {
    cnt = 0;
    for (let v of value) {
      ans.push(v[1]);
      cnt++;
      if (cnt === 2) break;
    }
  }
  return ans;
}
