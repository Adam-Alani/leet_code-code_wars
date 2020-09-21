function josephusSurvivor(n,k){
  var lst = Array(n).fill().map((e,i)=>i+1);
  var i = Math.floor(lst.length / k);
  while (i--) {
    lst.splice((i + 1) * k - 1, 1)
  }
  console.log(lst)
}


josephusSurvivor(7,3)