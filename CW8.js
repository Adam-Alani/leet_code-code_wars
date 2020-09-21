function sumIntervals(intervals){
  var list = [];
  intervals.forEach(elem =>{
    for (var i = elem[0]; i < elem[1]; i++) {
      list.push(i);
    }
  });
  list = [...new Set(list)]
  return(list.length)
}



var test1 = [[1,5]];
var test2 = [[1,4],[7, 10],[3, 5]];
sumIntervals(test2)
