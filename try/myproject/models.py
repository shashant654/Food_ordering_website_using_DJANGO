from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
          receipe_image = models.ImageField(upload_to='images',default='a')
          category_name = models.CharField(max_length=50,default='a')
          receipe_description = models.CharField(max_length = 50,null=True)

          def __str__(self):
                    return self.category_name


class Receipe(models.Model):
          receipe_name = models.CharField(max_length =50)
          receipe_description = models.CharField(max_length = 50)
          receipe_image = models.ImageField(upload_to='images',default='a')
          price = models.CharField(max_length=50,default='10')
          # choice = (('Burger','Burger',),('Snacks','Snacks'),('Bevearages','Bevearages'))
          category_name= models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
          # text = models.TextField( default='a')
          # boole= models.BooleanField(default=False)

          def __str__(self):
                    return self.receipe_name
                    
                    

class CartItem(models.Model):
          receipe_name = models.ForeignKey(Receipe,on_delete=models.CASCADE)
          quantity = models.IntegerField()
          price = models.IntegerField(null=True)
          owner = models.ForeignKey(User,on_delete=models.CASCADE)
          created_at = models.DateTimeField(auto_now_add=True)
        

          # def __str__(self):
                    # return self.receipe_name


class Order(models.Model):
          user = models.ForeignKey(User, on_delete=models.CASCADE)       
          fname = models.CharField(max_length=150, null=False)
          lname = models.CharField(max_length=150, null=False)
          email = models.CharField(max_length=150, null=False)
          phone = models.CharField(max_length=150, null=False)
          address = models.TextField(null=False)
          city = models.CharField(max_length=150, null=False)
          state = models.CharField(max_length=150, null=False)
          country = models.CharField(max_length=150, null=False)
          pincode = models.CharField(max_length=150, null=False)
          total_price = models.FloatField(max_length=150, null=False)
          payment_id = models.CharField(max_length=150, null=False)
          payment_method = models.CharField(max_length=150, default='COD')
          orderStatuses = (
                    ('pending','Pending'),
                    ('Out for Shipping', 'Out for Shipping'),
                    ('Completed','Completed'),
          )

          status = models.CharField(max_length=150, choices=orderStatuses, default='Pending')
          message = models.TextField(null= True) 
          tracking_no = models.CharField(max_length=150 , null=True)
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)



          def __str__(self):
                    return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
          order = models.ForeignKey(Order, on_delete=models.CASCADE)
          receipe = models.ForeignKey(Receipe, on_delete=models.CASCADE)
          price = models.FloatField(null=False)
          quantity = models.IntegerField(null=False)

          def __str__(self):
                    return '{} - {}'.format(self.order.id, self.order.tracking_no)


