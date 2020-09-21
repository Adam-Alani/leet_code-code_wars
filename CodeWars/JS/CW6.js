function smaller(arr) {
  n = arr.length;
  temp = [];
  count = new Array(n);
  for (var i = 0; i < n ; i ++) {count[i] = 0}
  for (var i = 0; i < n ; i ++) {
    for (var j = i+1 ; j < n; j++) {
      if (arr[j] < arr[i]) {
        count[i] += 1
      }
    }
  }
  return count
}

smaller([5, 4, 7, 9, 2, 4, 4, 5, 6])

/*
-

*/