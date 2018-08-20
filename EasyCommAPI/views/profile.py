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

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        print(user)

        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        
        print(user)
        serializer = profile(user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)