
function llenarPage(json){

	var cites = document.getElementById("quotes"); 
    for (i = 0; i < json.records.length; i++) {

        //lista de preguntas todas
        head = $('<div class="card-header" id="heading'+i+
            '"><a class="mb-0 "  data-toggle="collapse" data-target="#collapse'+i+'" >' +
            json.records[i].titulo+' </a></div>');
        contenido = $('<div class="card-body"><p>'+json.records[i].parrafo+'</p></div>');
        divContent = $('<div id="collapse'+i+'" class="collapse" data-parent="#accordion"> </div>');
        
        divContent.append(contenido);
        elemento = $('<div class="card "> </div>').append(head);
        elemento.append(divContent);
        $('#accordion').append(elemento);
        
    }
}

function cargarTermsJSON() {
	$.ajax({
		type:"GET",
		url:"/terms_load/",
		dataType:"json",
		success: llenarPage
	});
}

(function(){	
	
	cargarTermsJSON();

})();
