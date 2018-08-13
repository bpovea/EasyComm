function sorted(data){
    var sortedData = data.preguntas.slice(0);
    sortedData.sort(function(a,b) {
        return b.cantidad_visitas - a.cantidad_visitas;
    });
    return sortedData;
}

function loadQuestionsAnswer(json) {
    var cites = document.getElementById("quotes"); 
    for (i = 0; i < json.preguntas.length; i++) {

        //lista de preguntas todas
        head = $('<div class="card-header" id="heading'+i+
            '"><a class="mb-0 "  data-toggle="collapse" data-target="#collapse'+i+'" >' +
            json.preguntas[i].pregunta+' </a></div>');
        contenido = $('<div class="card-body">'+json.preguntas[i].respuesta+'<br><strong>Autor:<a href="">'+json.preguntas[i].autor+'</a></strong><br><strong>Fecha:</strong>'+json.preguntas[i].fecha +
            '<p><strong>Cantidad de vistas :</strong>'+json.preguntas[i].cantidad_visitas+'</p></div>');
        divContent = $('<div id="collapse'+i+'" class="collapse" data-parent="#accordion"> </div>');
        
        divContent.append(contenido);
        elemento = $('<div class="card "> </div>').append(head);
        elemento.append(divContent);
        $('#accordion').append(elemento);

        $('#list-preguntas-comunes').append($('<a class="list-group-item list-group-item-action " data-toggle="collapse" data-target="#collapse'+i+'" id="list-pregunta'+i+'-list" data-toggle="list" href="#list-pregunta'+i+'" role="tab" >'+json.preguntas[i].pregunta+'</a>'));

    }

    
    sortedData = sorted(json);
    for (i = 0; i < sortedData.length; i++) {
         $('#list-preguntas-frecuentes').append('<a data-toggle="collapse" data-target="#collapse'+(sortedData[i].id-1)+'" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center " role="tab" id="list-reciente'+i+'-list"  href="#list-reciente'+i+
            '">'+sortedData[i].pregunta+'<span class="badge badge-primary badge-pill">'+sortedData[i].cantidad_visitas+'</span></a>');
    }
     }

(function() {
    //cargar peguntas
     $.ajax({
        url: "/faqs_load/",
        type:"GET",    
        dataType : 'json',
        success : loadQuestionsAnswer,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos de las preguntas.');
        }
    });


})();
