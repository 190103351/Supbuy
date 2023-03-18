from django.shortcuts import render
from django.contrib.auth.models import User
from . models import Product,Category,SubCategory
from rest_framework.response import Response 
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

@api_view(['GET'])
def all_products(request):
    products_db = Product.objects.all()
    pr_serilized = ProductSerializer(products_db,many = True)
    
    return Response(pr_serilized.data)

@api_view(['GET'])
def get_by_id(request,pk):
    product = Product.objects.get(id = pk)
    ser = ProductSerializer(product)

    return Response(ser.data) 

@api_view(['POST'])
def add_product(request):
    serilizer = ProductSerializer(data = request.data)
    if serilizer.is_valid():
        serilizer.save()
        
    
    return Response({"status":'s'})

@api_view(['GET'])
def get_by_category(request,cat):
    s = SubCategory.objects.filter(name = cat)
    category_id = s.values()[0]['category_id']

    products = Product.objects.filter(category = category_id).all()
    serilizer = ProductSerializer(products)
    

    return Response(serilizer.data)


@api_view(['Post'])
def delete_by_id(request):
    product = Product.objects.delete(request)

@api_view(['Post'])
def add_category(request):
    serilizer = CategorySerializer(data = request.data)
    if serilizer.is_valid():
        serilizer.save()
        
        
    
    return Response({"status":'succed'})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })    
    

def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            

    
    
    return render(request,'products/register.html',{'form':form})
