var json_data = [];

$(document).ready(function(){
    data = {}
    data['date_from'] = $('#id_date_from').val();
    data['date_to'] = $('#id_date_to').val();
    
    /* grafico estadistico */
	$.ajax({
        url: "http://localhost:8000/api/report-orders/",
        type:"GET",  
        data :data,  
        dataType : 'json',
        success : function(json) {
            json_data = json;
            actualizar_grafico();            
        }
        ,error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos del gráfico estadistico.');
        }
    });
});

function actualizar_grafico(){
    unidades = "$   "
    opcion ="totales";
    grafico = json_data[opcion]
    if($('#opciones').val() == "1"){
        unidades = "cantidad de productos"
        opcion = "productos";
        grafico = [];
        for (let key of Object.keys(json_data[opcion])) {
            data = {}
             data['nombre'] = key;
             data['valor'] = json_data[opcion][key];
             grafico.push(data);
        }
    }else if($('#opciones').val() == "2"){
        opcion = "socios";
    }
    if (grafico.length > 0){
        renderGraph(grafico,unidades);    
    }else{
        $('#graph').html("No se han encontrado resultados. ");
    }
    
}

document.getElementById("opciones").onchange = actualizar_grafico;