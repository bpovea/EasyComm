id = ""

function agregarCategorias(lista){
    $("table").append(""); 
    html = "<tr><th># </th><th>Nombre </th><th>Descripción</th><th>Editar</th><th>Eliminar</th></tr>";
    for (var i = 0; i < lista.length; i++) {
        html +='<tr id="row'+ lista[i].id +'"><th>'+(i+1)+'</th><th>' + lista[i].name +"</th>";
        html +="<th>" + lista[i].description +"</th>";
        html += '<th><i class="fa fa-edit fa-2x m-1" onclick="editar(row'+ lista[i].id +')"></i></th>' ;
        html += '<th><i class="fa fa-trash-o fa-2x m-1" onclick="eliminar(row'+ lista[i].id +')"></i></th>' ;
        html +="</tr>";     
    }
    $("table").append(html);  
};
//
function listarCategorias(){
    $.ajax({
        url: "http://127.0.0.1:8000/api/products-categories/",
        type:"GET",   
        dataType : 'json',
        success :agregarCategorias,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar la lista de categorias.');
        }
    });

}
$(document).ready(function() {
    listarCategorias();
});

function updateID(row){
    id = $(row).attr("id");
    var fila =$("#"+id+" th");
    arreglo = id.split('row');
    id = arreglo[1];
}

function crearCategoria() {
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    data ={
        "name" : $("#name").val(),
        "description":$("#description").val()
    }
    $.ajax({
        url: "http://127.0.0.1:8000/api/products-categories/",
        type:"POST",   
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data: data,
        success :function(data) {
            alert('Se creó correctamente la categoria.');
            $("#mostrarmodal").modal("hide");
            window.location.replace("/categories/");
        },
        error : function(xhr, status) {
            console.log(xhr);
            alert('Disculpe, existió un problema al cargar la lista de categorias.');
        }
    });
 } 

function nuevo(){
    $("#mostrarmodal").modal("show");
    $(".modal-dialog").attr("style","height: 378px; z-index: 2;");
    $("#boton").html("Crear");
    $("#boton").attr("onclick","crearCategoria()");
    $("#name").val("");
    $("#description").val("");

}

function editar(row){
    $("#boton").html("Guardar Cambios");
    $("#boton").attr("onclick","guardarCambios()");
    id = $(row).attr("id");
    var fila =$("#"+id+" th");
    $("#name").val(fila[1].innerHTML);
    $("#description").val(fila[2].innerHTML);
    arreglo = id.split('row');
    id = arreglo[1];
    $("#mostrarmodal").modal("show");
    $(".modal-dialog").attr("style","height: 378px; z-index: 2;");
}

function guardarCambios(){
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    data ={
        'id':id,
        "name" : $("#name").val(),
        "description":$("#description").val()
    }
    $.ajax({
        url: "http://127.0.0.1:8000/api/products-categories/" + id + "/",
        type:"PUT",   
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data: data,
        success :function(data) {
            alert('Se actualizó correctamente la categoria.');
            $("#mostrarmodal").modal("hide");
            window.location.replace("/categories/");
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al guardar los cambios de categorias.');
        }
    });
}



function eliminar(row){
    updateID(row);
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url: "http://127.0.0.1:8000/api/products-categories/" + id + "/",
        type:"DELETE",   
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        success :function(data) {
            alert('Se eliminó correctamente la categoria.');
            $("#mostrarmodal").modal("hide");
            window.location.replace("/categories/");
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar la lista de categorias.');
        }
    });
}
