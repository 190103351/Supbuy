from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class CustomUser(models.Model):
    user_types = [
        ('SUPL','Supplier'),
        ('BUYER','Buyer'),
        ('ADM','Admin')
    ]
    type = models.CharField(max_length = 5,choices=user_types,default='SUPL')
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name






class Product(models.Model):
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    product_img = models.ImageField(upload_to='base/static/media',null=True,default=None)
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE,related_name='category_name')
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    
    def __str__(self) -> str:
        return self.name + " \n"+self.description[:10]
    
    def info(self):
        return self.name + '\n'+self.description
    
    


    

class Order(models.Model):
    client   =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='client')
    address  =  models.CharField(max_length =250)
    city     =  models.CharField(max_length = 100)
    created  =  models.DateTimeField(auto_now_add = True)
    update   =  models.DateTimeField(auto_now = True)
    product  =  models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity =  models.PositiveIntegerField(default=1)



    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'
    
    def  get_cost(self):
        return self.quantity * self.product.price

    



    


class Notification(models.Model):
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user')
    accepted = models.PositiveIntegerField(default=3)
    # 1 is accepted 2 is rejected 3 is default
    order = models.ForeignKey(Order,on_delete=models.CASCADE)


    def __str__(self) -> str:
        status = ['accepted','rejected','default']
        return f'{self.to_user.username} - {self.from_user.username} {status[self.accepted-1]}'


class Agreement(models.Model):
    buyer = models.FileField(upload_to='base/static/media')
    supplier = models.FileField(upload_to='base/static/media/')
    checked = models.BooleanField()
    notification = models.ForeignKey(Notification,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.buyer.username} <-> {self.supplier.username} {self.checked}'


