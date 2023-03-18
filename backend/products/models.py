from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

# class User(AbstractUser):
#     info = models.TextField()
    
# class Supplier(User):
#     license_data = models.ImageField(upload_to='media/',default=None,null = True)

    

# class Buyer(User):
#     pass




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null = True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    
    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='media/',default=None,null=True)
    in_basket = models.BooleanField()
    category = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True)
    count = models.IntegerField(default = 1)

    def __str__(self) -> str:
        return self.name



    

