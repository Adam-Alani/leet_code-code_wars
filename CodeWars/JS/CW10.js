function reverseNumber(n) {
  str = n.toString();
  res = "";
  for (var i = str.length-1; i >= 0 ; i--) {
    res += str[i];
  }
  if (n < 0) {return parseInt(res)*-1;}
  else {return parseInt(res); }
}
reverseNumber(1230)