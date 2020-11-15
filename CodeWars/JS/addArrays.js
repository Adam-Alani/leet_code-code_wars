function addArrays(array1, array2) {

  let arrayToNumber1 = parseInt(array1.join('')) || [] ;
  let arrayToNumber2 = parseInt(array2.join('')) || [] ;

  let res = Array.from(String(arrayToNumber1 + arrayToNumber2 ), Number ) ;

  for (i = 0 ; i < res.length ; i++ ) {
    if (isNaN(res[i])) {
      res[i+1] *= -1
      res.splice(i,1)
    }
  }
  return res.filter( value => !Number.isNaN(value) );
}


console.log(addArrays([67],[]))