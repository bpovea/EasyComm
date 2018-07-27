from django.core import serializers
from django.http import JsonResponse
from oscar.core.loading import get_model

City = get_model('address', 'city')

def city_list(request):
    cities = []
    province = request.GET.get('province', None)
    if province:
        cities = City.objects.filter(province=province)
    return JsonResponse(serializers.serialize('json', cities), safe=False)