from django.contrib import admin
from .models import Receipe,Category,CartItem,Order,OrderItem

# Register your models here.

admin.site.register(Receipe)
admin.site.register(Category)

admin.site.register(CartItem)

class Myorders(admin.ModelAdmin):
          list_filter=['user','address','total_price','status','tracking_no']
          list_display=['user','address','total_price','status','tracking_no']
          list_editable=['status']
          list_display_links=['tracking_no']
          
admin.site.register(Order,Myorders)
admin.site.register(OrderItem)

