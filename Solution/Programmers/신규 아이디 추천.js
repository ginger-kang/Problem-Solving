function solution(new_id) {
  new_id = new_id
    .toLowerCase()
    .replace(/[^a-z0-9-_.]/g, "")
    .replace(/\.+/g, ".")
    .replace(/^\.+|\.$/g, "");

  if (!new_id) new_id += "a";

  new_id = new_id.slice(0, 15).replace(/\.$/g, "");
  if (new_id.length < 3) {
    const last = new_id[new_id.length - 1];
    while (new_id.length < 3) {
      new_id += last;
    }
  }

  return new_id;
}
