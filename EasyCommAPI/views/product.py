from oscarapi.views import product
from oscarapi.serializers import ProductLinkSerializer
from rest_framework import generics
from oscar.core.loading import get_class, get_model
from oscarapi import serializers
from EasyCommAPI.serializers import product_detail_serializer
from rest_framework.views import APIView

Selector = get_class('partner.strategy', 'Selector')

__all__ = (
    'ProductList', 'ProductDetail',
)

Product = get_model('catalogue', 'Product')


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = product_detail_serializer
    
    
    def get_queryset(self):
        """
        Allow filtering on structure so standalone and parent products can
        be selected separately, eg::
            http://127.0.0.1:8000/api/products/?structure=standalone
        or::
            http://127.0.0.1:8000/api/products/?structure=parent
        """
        qs = super(ProductList, self).get_queryset()
        structure = self.request.query_params.get('structure')
        if structure is not None:
            return qs.filter(structure=structure)
        return qs

    def post(self, request, format=None):
        serializer = product_detail_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer



class producto_detalle(APIView):

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        servicio = Servicio.objects.get(nombre=request.POST['servicio'])
        if not usuario.servicios.filter(servicio=servicio):
            usuarioServicio = ServicioUsuario(usuario=usuario,servicio=servicio,fecha = datetime.datetime.strptime(request.POST['registro'],"%Y-%m-%d"),
                direccion=request.POST['direccion'])
            usuarioServicio.save() 
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        else:
            return Response("Ya esta registrado ese servicio", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)