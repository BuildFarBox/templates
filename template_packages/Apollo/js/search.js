function search() {
	if (document.getElementById('search_value').value) {
	  location.href = 'http://' + location.host + '?s=' + document.getElementById('search_value').value;
	}
	return false;
 }