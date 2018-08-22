var json_data = [];

$(document).ready(function(){
    tabla = $("#example").clone();
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

tabla=[]
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
        cambiarTabla();
    }else if($('#opciones').val() == "2"){
        cambiarTablaUsuarios();
    }else{
        $("table").replaceWith(tabla);
    }
    if (grafico.length > 0){
        renderGraph(grafico,unidades);    
    }else{
        $('#graph').html("No se han encontrado resultados. ");
    }
    
}

document.getElementById("opciones").onchange = actualizar_grafico;


function cambiarTabla(){
    html = '<table class="table table-striped table-bordered table-hover"><tr><th>producto</th><th>Cantidad</th></tr>';

    $.ajax({
        url: "http://localhost:8000/api/report-ordes-noSQL/",
        type:"GET",  
        data :data,  
        dataType : 'json',
        success : function(json) {
            for (let key of Object.keys(json["productos"])) {
                html += '<tr><td>' + key + '</td><td>'+ json["productos"][key] + '</td></tr>';
            }
            html+= "</table>";
            $("table").replaceWith(html);

            
        },error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos.');
        }
    });
}

function cambiarTablaUsuarios(){
    html = '<table class="table table-striped table-bordered table-hover"><tr><th>Usuario</th><th>totales</th></tr>';

    $.ajax({
        url: "http://localhost:8000/api/report-users-noSQL/",
        type:"GET",  
        data :data,  
        dataType : 'json',
        success : function(json) {
            for (let key of Object.keys(json["usuarios"])) {
                html += '<tr><td>' + key + '</td><td>$'+ json["usuarios"][key] + '</td></tr>';
            }
            html+= "</table>";
            $("table").replaceWith(html);

            
        },error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos.');
        }
    });
}