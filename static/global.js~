function getCookie(name) {
	  var cookieValue = null;
		if (document.cookie && document.cookie != '') {
		    var cookies = document.cookie.split(';');
		    for (var i = 0; i < cookies.length; i++) {
		        var cookie = jQuery.trim(cookies[i]);
		        // Does this cookie string begin with the name we want?
		        if (cookie.substring(0, name.length + 1) == (name + '=')) {
		            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		            break;
		        }
		    }
		}
		return cookieValue;
}
function getURLParameter(name) {
  return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
}

function getCondition(conditionId){
	if(conditionId == 1){
		return "New - In Box";
	} else if (conditionId == 2){
		return "Used - Like new";
	} else if (conditionId == 3){
		return "Used - Moderate";
	} else if (conditionId == 4){
		return "Used - Poor";
	} else if (conditionId == 5){
		return "Broken";
	}
	return "Error - incorrect conditionId";
}

function getConditionId(condition){
	if(condition == "New - In Box"){
		return 1;
	} else if (condition == "Used - Like new"){
		return 2;
	} else if (condition == "Used - Moderate"){
		return 3;
	} else if (condition == "Used - Poor"){
		return 4;
	} else if (condition == "Broken"){
		return 5;
	}
}
