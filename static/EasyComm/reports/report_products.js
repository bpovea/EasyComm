var json_data = [];

$(document).ready(function(){
    //obteniendo parametros de consulta
    $('span.form-group:nth-child(3)').css('display','none');
    $('span.form-group:nth-child(4)').css('display','none');
    

    /* grafico estadistico */
	$.ajax({
        url: "http://127.0.0.1:8000/api/report-products/",
        type:"GET",    
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
    opcion = "num_views"
    if($('#opciones').val() == "1"){
        opcion = "num_basket_additions";
    }else if($('#opciones').val() == '2'){
        opcion = "num_purchases";
    }
    grafico = [];
    for (i = 0; i < json_data.length; i++) {
        data = {}
        data['nombre'] = json_data[i].product.title;
        data['valor'] = json_data[i][opcion];
        grafico.push(data);
    }
    unidades = "cantidad";
    if (grafico.length > 0){
        renderGraph(grafico,unidades);    
    }else{
        $('#graph').html("No se han encontrado resultados. ");
    }
    
}
document.getElementById("opciones").onchange = actualizar_grafico;