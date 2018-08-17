from oscar.core.loading import get_class, get_model
from oscarapi import serializers
from EasyCommAPI.serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser


from oscar.core.compat import (get_user_model)


User = get_user_model()

class profile_details(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = profile(user)
        return Response(serializer.data)