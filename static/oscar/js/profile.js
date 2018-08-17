
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

function cargarProfile(data){
    console.log(data);
};