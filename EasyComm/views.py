from django.shortcuts import render,render_to_response,get_object_or_404,redirect


def home(request):
	return render(request,'../templates/EasyComm/index.html')


def about_us(request):
	return render(request,'../templates/EasyComm/about_us_g3.html')

def contact_us(request):
	return render(request,'../templates/EasyComm/contact_us.html')

def faqs(request):
	return render(request,'../templates/EasyComm/faqs.html')