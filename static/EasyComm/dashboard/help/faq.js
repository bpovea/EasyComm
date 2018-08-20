csrf = $("#csrf_token>input")[0].value

$(".edit").click(function(ev){
    id = $(ev.currentTarget).attr("pk")
    $.ajax({
        url: "http://localhost:8000/help/api/faqs/"+id,
        type:"GET",    
        dataType : 'json',
        success : function(rsp){
            renderDetail(rsp)
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos del FAQ.');
        }
    });
})

$(".del").click(function(ev){
    id = $(ev.currentTarget).attr("pk")
    $.ajax({
        url: "http://localhost:8000/help/api/faqs/"+id,
        type:"DELETE",
        headers: {"X-CSRFToken":csrf},
        success : function(){
            location.reload();
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al eliminar FAQ.');
        }
    });
})

$("#save").click(function(){
    question = $("#qst-new").val()
    answer = $("#rsp-new").val()
    if ( document.getElementById("st-new").checked ){
        status = 1
    }else{
        status = 0
    }
    data = {
        question : question,
        answer : answer,
        status: status
    }
    $.ajax({
        url: "http://localhost:8000/help/api/faqs/",
        type:"POST",
        data: data,
        headers: {"X-CSRFToken":csrf}, 
        success : function() {
            location.reload();
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema creando el FAQ.');
        }
    });
})

$("#upd").click(function(ev){
    id = $(ev.currentTarget).attr("id_faq")
    question = $("#qst-detail").val()
    answer = $("#rsp-detail").val()
    if ( document.getElementById("st-detail").checked ){
        status = 1
    }else{
        status = 0
    }
    data = {
        question : question,
        answer : answer,
        status: status
    }
    $.ajax({
        url: "http://localhost:8000/help/api/faqs/"+id,
        type: "PUT",
        data: data,
        headers: {"X-CSRFToken":csrf}, 
        success : function() {
            location.reload();
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema actualizando el FAQ.');
        }
    });
})



function renderDetail(rsp){
    $("#faq-id").text(rsp.id)
    $("#upd").attr("id_faq",rsp.id)
    $("#qst-detail").val(rsp.question)
    $("#rsp-detail").val(rsp.answer)
    if(rsp.status == 1){
        document.getElementById("st-detail").checked =  true
    }else{
        document.getElementById("st-detail").checked = false
    }

}