function cargarBotones1(){
    $('#profileBotones1').show();
    $('#profileBotones2').hide();
}
function cargarBotones2(){
    $('#profileBotones1').hide();
    $('#profileBotones2').show();
}

function llenarTablaProfile(data){
    //console.log(data);
    let htmlTablaProfile = '';

    htmlTablaProfile += '<tr>';
    htmlTablaProfile +=    '<th>first name</td><td id="firstname">'+data['first_name']+'</td>';
    htmlTablaProfile += '</tr>';
    htmlTablaProfile += '<tr>';
    htmlTablaProfile +=    '<th>last name</td><td id="lastname">'+data['last_name']+'</td>';
    htmlTablaProfile += '</tr>';
    htmlTablaProfile += '<tr>';
    htmlTablaProfile +=    '<th>email</td><td id="email">'+data['email']+'</td>';
    htmlTablaProfile += '</tr>';

    $("#serviciosTBody").html(htmlTablaProfile);

};

function cargarProfile(){
    $.ajax({
        url: "http://127.0.0.1:8000/api/profile/" + $('#userID').val(),
        type:"GET",    
        dataType : 'json',
        success : llenarTablaProfile,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos del producto.');
        }
    });
}

function vaciarTabla(){
    $("#serviciosTBody").html("");
}

function editarPerfil(element){
    
    let htmlFormForProfile = '';
    htmlFormForProfile += 'First name:<br>'
    htmlFormForProfile += '<input type="text" id="formFirstName" name="firstname" value="'+$('#firstname').text()+'"><br>';
    htmlFormForProfile += 'Last name:<br>'
    htmlFormForProfile += '<input type="text" id="formLastName" name="lastname" value="'+$('#lastname').text()+'"><br>';
    htmlFormForProfile += 'Email:<br>'
    htmlFormForProfile += '<input type="text" id="formEmail" name="email" value="'+$('#email').text()+'">';

    vaciarTabla();
    cargarBotones2();
    $('#formForUpdate').html(htmlFormForProfile);
    $('#formForUpdate').show();

}

function reloadAfterUpdate(){

    cargarProfile();
    $('#formForUpdate').hide();
    cargarBotones1();
}

function guardarPerfil(){
    info ={
        "first_name": $('#formFirstName').val(),
        "last_name": $('#formLastName').val(),
        "email": $('#formEmail').val(),
    }
    console.log(info);
    
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    console.log(crf_token);
    $.ajax({
        url: "http://127.0.0.1:8000/api/profile/" + $('#userID').val()+"/",
        type:"PUT",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :reloadAfterUpdate,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al actualizar sus datos.');
        }
    });

    reloadAfterUpdate();
}

function eliminarPerfil(){
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
     $.ajax({
        url: "http://127.0.0.1:8000/api/profile/"+$("#userID").val()+"/",
        type:"DELETE",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        success :function(respuesta) {
            window.location.replace("http://127.0.0.1:8000/home/");
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al eliminar sus datos.');
        }
    });

    reloadAfterUpdate();
}

$(document).ready(function(){
    
    cargarProfile();
    cargarBotones1();
    $('#formForUpdate').hide();
});