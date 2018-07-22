$(document).ready(function(){
	$(".alertinner").each(function(){
		createalert(this.innerHTML,8000);
	});
});

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function createalert(message, timedelay, type){
	if (timedelay==null){ timedelay=2000;}
	if (type==null){ type="danger";}
	$.notify({
		// options
		message: message,
		//url: 'https://github.com/mouse0270/bootstrap-notify',
	},{
		// settings
		delay: timedelay,
		type: type,
		placement: {
			from: "bottom",
			align: "right"
		},
		animate: {
			enter: 'animated fadeInDown',
			exit: 'animated fadeOutUp'
		},
		mouse_over: 'pause',
		template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0} mensaje" role="alert">' +
			'<button type="button" aria-hidden="true" class="close" data-notify="dismiss" style="color:white;">×</button>' +
			'<span data-notify="icon"></span> ' +
			'<span data-notify="title">{1}</span> ' +
			'<span data-notify="message" class="message">{2}</span>' +
			'<div class="progress" data-notify="progressbar">' +
				'<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
			'</div>' +
			'<a href="{3}" target="{4}" data-notify="url"></a>' +
		'</div>'
	});
}