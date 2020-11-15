function pickPeaks(arr) {
  var difflist = [];
  var res = [];
  var resind = [];


  for (i = 0 ; i < arr.length -1 ; i++) {
    if (arr[i] < arr[i+1]) {
      difflist.push(1);
    }
    else if (arr[i] == arr[i+1]) {
      difflist.push(0);
    }
    else {difflist.push(-1);}
  }

  let c = 0
  
  for (j = 0 ; j < arr.length -2 ; j++) {
    
    if (difflist[j] == 1 && difflist[j+1] == -1 ) {
      res.push(arr[j+1]);
      resind.push(j+1);
    }
    
    if (difflist[j] == 1 && difflist[j+1] == 0) {
      if (difflist.splice[j+1] == [difflist[j+1]] ){
        break
      }
      c = j+1
      while (difflist[c] == 0 && c < (arr.length-2)) {
        c = c+1;
      }
      if (difflist[c] == -1) {
        res.push(arr[j+1]);
        resind.push(j+1);
      }
    }
  }

  return {
    pos: resind ,
    peaks: res
  };
}

console.log(pickPeaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))


