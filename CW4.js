function kebabize(str) {
  str = str.replace(/\d+/g, '');
  str = str.split(/(?=[A-Z])/)
  return (str.join('-')).toLowerCase()
 }
  
