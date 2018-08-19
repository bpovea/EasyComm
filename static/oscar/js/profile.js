function editarPerfil(){
    $("#mostrarmodal").modal("show");
    $(".modal-dialog").attr("style","height: 378px; z-index: 2;");
}

function cargarProfile(data){
    html_nombre = "<tr><th>Nombre</th><td>" + data.first_name  + " "+ data.last_name + "</td></tr>";
    html_correo = "<tr><th>Correo electrónico</th><td>" + data.email + "</td></tr>";
    html_fecha = "<tr><th>Fecha de registro</th><td>" + data.date_joined + "</td></tr>";
    html_fecha_ultimo = "<tr><th>Último unicio de sesión</th><td>" + data.last_login + "</td></tr>";
    $("table tbody").append(html_nombre);
    $("table tbody").append(html_correo);
    $("table tbody").append(html_fecha);
    $("table tbody").append(html_fecha_ultimo);
};

$(document).ready(function(){
    
    $.ajax({
        url: "http://127.0.0.1:8000/api/profile/" + $('#id').val(),
        type:"GET",    
        dataType : 'json',
        success : cargarProfile,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos del producto.');
        }
    });
	
});


