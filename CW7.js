var maxSequence = function(arr){
  if (arr.length === 0 ) {return 0}
  else {
    var current = 0
    var largest = 0
    for (var num of arr) {
      current = Math.max(0,(current+num))
      largest = Math.max(largest, current)
    }
    return(largest)
  }
  }
