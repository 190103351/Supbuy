from django.urls import path,include
from .import views


urlpatterns = [
    path('users/',views.ListUsers.as_view()),
    path('all/',views.all_products,name='all_products'),
    path('add/',views.add_product),
    path('<int:pk>/',views.get_by_id),
    path('<str:cat>/',views.get_by_category),
    path('token-auth/', views.CustomAuthToken.as_view()),
    path('register',views.register_user),

]
