from django.shortcuts import render
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view
from django.db.models import Q 
from . import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from .forms import ProductForm
from .models import Product,CustomUser,Category,Notification,Order,Agreement

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer

def log_out(request):
    pass



@api_view(['GET'])
def all_categories(request):
    categories = Category.objects.all()
    serial_categories = serializers.CategorySerializer(categories,many = True)
    return Response(serial_categories.data)


@api_view(['GET'])
def get_by_category_name(request):
    category_name = request.GET.get('category_name') if request.GET.get('category_name') != None else ''
    products = Product.objects.filter(category__name__icontains = category_name).all()
    ser_products = serializers.ProductSerilizer(products,many=True)
    return Response(ser_products.data)


@api_view(['GET'])
def get_notifications_from_user(request):
    username = request.GET.get('username')
    notifications = Notification.objects.filter(from_user__username__icontains = username).all()
    ser = serializers.NotificationSerializer(notifications,many = True)
    return Response(ser.data)




@api_view(['GET'])
def get_notifications_to_user(request):
    username = request.GET.get('username')
    notifications = Notification.objects.filter(to_user__username__icontains = username).all()
    ser = serializers.NotificationSerializer(notifications,many = True)
    return Response(ser.data) 


@api_view(['POST'])
def delete_notification(request,pk):
    if request.method == 'POST':
        notif = Notification.objects.get(pk)
        if notif:
            notif.delete()
            notif.save()
    return Response({
        f'succes {pk}':'deleted'
    })



@api_view(['GET'])
def all_agreement(request):
    agreements = Agreement.objects.filter(check = False)
    return serializers.AgreementSerializer(agreements,many=True).data



class AddProductView(views.APIView):


    def post(self,request):
        product_ser = serializers.ProductSerilizer(data = request.data)

        if Product.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
        if product_ser.is_valid():
            product_ser.save()
        
        
        
        return Response({
            "status":'saved'
            }
        )



@api_view(['GET'])
def get_product(request):
    product_name = request.GET.get('product-name')
    product = Product.objects.filter(name = product_name).first()
    if product:
        return Response(serializers.ProductSerilizer(product).data)
    return Response({})



@api_view(['GET'])
def current_user_orders(request):
    username = request.GET.get('username')
    orders = Order.objects.filter(client__username=username).all()
    return Response(serializers.OrderSerializer(orders).data)

