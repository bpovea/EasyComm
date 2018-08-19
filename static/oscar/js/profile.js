

$(document).ready(function(){

	console.log($('#userID').val());
    
    $.ajax({
        url: "http://127.0.0.1:8000/api/profile/" + $('#userID').val(),
        type:"GET",    
        dataType : 'json',
        success : cargarProfile,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos del producto.');
        }
    });
	
});


function editarServicioDeUsuario(element){
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={
        "first_name": $('#first_name').val(),
        "last_name": $('#last_name').val(),
        "email": $('#email').val(),
    }
    
    $.ajax({
        url: "http://127.0.0.1:8000/api/profile/" + $('#userID').val(),
        type:"PUT",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
            alert("Servicio asociado al usuario modificado con éxito");
            $("#mostrarmodal").modal("hide");
            cargarProfile();
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al guardar los datos del producto.');
        }
    });
}

function eliminarServicioDeUsuario(element){
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={
        "servicio":$("#servicio").val(),
    }
    $.ajax({
        url: "/usuario_servicio/"+$("#id").val(),
        type:"DELETE",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
            alert("Servicio asociado al usuario eliminado con éxito");
            $("#mostrarmodal").modal("hide");
            actualizarListaServicios();
        },
        error : function(xhr, status) {
            alert(xhr['responseJSON']);
        }
    });
}


function cargarProfile(data){
    console.log(data);
    let htmlTablaProfile = '';
    htmlTablaProfile += '<tr>';
    htmlTablaProfile +=    '<th>first name</td>';
    htmlTablaProfile +=    '<td>'+data['first_name']+'</td>';
    htmlTablaProfile += '</tr>';
    htmlTablaProfile += '<tr>';
    htmlTablaProfile +=    '<th>last name</td>';
    htmlTablaProfile +=    '<td>'+data['last_name']+'</td>';
    htmlTablaProfile += '</tr>';
    htmlTablaProfile += '<tr>';
    htmlTablaProfile +=    '<th>email</td>';
    htmlTablaProfile +=    '<td>'+data['email']+'</td>';
    htmlTablaProfile += '</tr>';
    $("#serviciosTBody").html(htmlTablaProfile);

};