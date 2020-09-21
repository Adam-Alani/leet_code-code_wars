function pigIt(str){
  str = str.split(' ');
  for(var i = 0 ; i <str.length ; i++) {
    if(/[a-zA-Z]/.test(str[i])) {
      str[i] = str[i].slice(1) + str[i][0] + 'ay';
    }
  }
  return str.join(' ');
}



pigIt('Pig latin is cool');