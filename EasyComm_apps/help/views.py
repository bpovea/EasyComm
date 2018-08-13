from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

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
