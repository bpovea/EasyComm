function presentar(imagen){
	/*$("#modal").modal("show");
	var captionText = document.getElementById("caption1");
	captionText.innerHTML = $("#"+imagen).attr('alt');*/
	$("#imagen-modal").attr("src",$("#"+imagen).attr('src'));
}