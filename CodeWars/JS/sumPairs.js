function sumPairs(ints, s) {
  for (i = 0 ; i < ints.length ; i++ ) {
    for (j = 1 ; j < ints.length ; j++) {
      if (ints[i] + ints[j] == s) {
        return [ints[i] , ints[j]]
      }
    }
  }
  return undefined ;
}


console.log(sumPairs([10, 5, 2, 3, 7, 5], 10))