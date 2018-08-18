from django.shortcuts import render,render_to_response,get_object_or_404,redirect
from django.http import JsonResponse
import json
from oscar.core.loading import get_class, get_model


Partner = get_model('partner', 'Partner')

def home(request):
	partners = Partner.objects.all()[:3]
	return render(request,'../templates/EasyComm/index.html',{'partners':partners})


def about_us(request):
	return render(request,'../templates/EasyComm/about_us_g3.html')

def contact_us(request):
	return render(request,'../templates/EasyComm/contact_us.html')

def faqs(request):
	return render(request,'../templates/EasyComm/faqs.html')


def partners(request):
	partners = Partner.objects.all()
	return render(request,'../templates/EasyComm/partners.html',{'partners':partners})


def faqs_load(request):
	path_json = "data/faqs.json"
	with open(path_json, 'r') as f:
		array = json.load(f)
		return JsonResponse(array)