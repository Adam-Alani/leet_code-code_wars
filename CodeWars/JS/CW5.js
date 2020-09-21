function isPangram(string) {
  var regex = /([a-z])(?!.*\1)/g;
  return (string.match(regex) || []).length === 26;
}