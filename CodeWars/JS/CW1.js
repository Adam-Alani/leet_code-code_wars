
function alphabetPosition(text) {
	var alphabet =  "abcdefghijklmnopqrstuvwxyz";
	var res = '';
	for (var i = 0; i < text.length; i++){
		for (var j = 0; j < alphabet.length ; j++){
		if (text[i] === alphabet[j]) {
			res.push(alphabet.indexOf[j]);
		}
		}
	}
  return res;
	}
