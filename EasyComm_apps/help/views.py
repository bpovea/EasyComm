from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from .models import Faq
from .serializers import FaqSerializer


class FaqView(TemplateView):
    template_name = 'help/faq.html'

    def get_context_data(self, **kwargs):
        context = super(FaqView, self).get_context_data(**kwargs)
        context['active_tab'] = 'faq'
        context['faqs'] = Faq.objects.filter(status=1)
        return context

#  API
@csrf_exempt 
@api_view(['GET', 'POST'])
def faqList(request):
  if request.method == 'GET':
    faqs = Faq.objects.filter(status=1)
    serializer = FaqSerializer(faqs, many = True)
    return JsonResponse(serializer.data, safe = False)

  elif request.method == 'POST':
    serializer = FaqSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def faqDetail(request, pk):
    try:
        faq = Faq.objects.get(pk=pk)
    except faq.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FaqSerializer(faq)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FaqSerializer(faq, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)