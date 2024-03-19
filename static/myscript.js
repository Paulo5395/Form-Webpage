$(document).ready(function() {
	
});

function toggleHidden() {
	var hiddenElement = document.getElementById("user-password")
	
	if(hiddenElement.type === "password") {
		hiddenElement.type = "text";
	}

	else {
		hiddenElement.type = "password";
	}
}