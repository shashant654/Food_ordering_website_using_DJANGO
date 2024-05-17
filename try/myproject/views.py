from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import Receipe,Category,CartItem
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required

import os


# def AddToCart(request):
#       ob = Receipe.objects.all()
#       return render(request,"cart.html",{'Receipe':ob})




def showw(request):
      #     d=Receipe.objects.all()
      #     for i in d:
      #               i.receipe_image=os.path.basename(i.receipe_image.url)
      #     return render(request,"show.html",{'data':d})  
      #     ---------------------------------------------------------------------------- 

              
          if request.method == "POST":
             category1 = request.POST.get('Category')
             cat = Category.objects.get(category_name = category1)

             if cat:
                  data = Receipe.objects.filter(category_name = cat)
                  print(data)

                  for i in data:                 
                    i.receipe_image=os.path.basename(i.receipe_image.url)
                    print(i.category_name)
             return render(request,"show.html",{'data':data}) 

          return render(request,"menu.html",{'data':data})          


# Create your views here.


def login_page(request):

      if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not User.objects.filter(username= username).exists():
                  messages.error(request, 'Invalid Username')
                  return redirect('/login/')

            user = authenticate(username = username,password=password)      

            if user is None:
                  messages.error(request, 'Invalid Password')
                  return redirect('/login/')

            else:
                  login(request, user)    
                  return redirect('/project/')  


      return render(request,'login.html')


#       ----------------------------------------- 
def logout_page(request):
      logout(request)
      return redirect('/login/')


def register(request):

      if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = User.objects.filter(username = username)

            if user.exists():
                  messages.info(request,'username already taken')
                  return redirect('/register/')

            user = User.objects.create(
                  first_name = first_name,
                  last_name = last_name,
                  username = username,
            )

            user.set_password(password)
            user.save()

            messages.info(request,'Account created successfully')

            return redirect('/login/')
      
      return render(request,'register.html')




def projectt(request):
          return render(request,'project.html')

def aboutt(request):
          return render(request,'about.html')

@login_required(login_url='/login/')
def bookingg(request):
          return render(request,'booking.html')

def cheff(request):
          return render(request,'chef.html')

def contactt(request):
          return render(request,'contact.html')

def featuree(request):
          return render(request,'feature.html')
# def myorders(request):
      # orderobj=Order.objects.filter(user=request.user)
      # orders=''
      # for orobj in orderobj:
      #       orders=OrderItem.objects.filter(order=orobj)
      # return render(request,'myorder.html',{"orders":orders})
      # pass

def myorders(request):
      # return render(request,'myorder.html')
      orderobj=Order.objects.filter(user=request.user)
      orders=[]
      for orobj in orderobj:
            orders.append({
                  'order':orobj,
                  'items':OrderItem.objects.filter(order=orobj)
            })
            # orders=OrderItem.objects.filter(order=orobj)
      return render(request,'myorder.html',{"orders":orders})
      pass


def orderr(request):
      cartData=CartItem.objects.filter(owner=request.user)

      tprice=0
      for d in cartData:
            tprice+=d.price
      if request.method=='POST':
            import random
            user=request.user
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')
            phone=request.POST.get('Phone')
            address=request.POST.get('Address')
            city=request.POST.get('City')
            state=request.POST.get('State')
            country=request.POST.get('Country')
            pincode=request.POST.get('Pin')
            total_price=tprice
            payment_id=f'Pay{random.randint(111111,999999)}'
            # payment_method=request.POST.get('COD')
            message='Order Placed !'
            tracking_no=f'Order{random.randint(111111,999999)}'

            orderD=Order() 
            # here Order() class ko orderD variable me initialize kr diye
            # here Order.objects.create(-------------------------) aise v create kr skte thee
 
            orderD.user=request.user
            orderD.fname=fname
            orderD.lname=lname
            orderD.email=email
            orderD.phone=phone
            orderD.address=address
            orderD.city=city
            orderD.state=state
            orderD.country=country
            orderD.pincode=pincode
            orderD.total_price=total_price
            orderD.payment_id=payment_id
            # orderD.payment_method=payment_method
            orderD.message=message
            orderD.tracking_no=tracking_no
            orderD.save()

            for carti in cartData:  
                  OrderItem.objects.create(receipe=carti.receipe_name,order=orderD,price=carti.price,quantity=carti.quantity)
                  
            CartItem.objects.filter(owner=request.user).delete()

            return redirect('myorders')
      return render(request,'order.html',{"cartdata":cartData,"tprice":tprice})


def cartt(request):
      if request.method == 'POST':
            receipe_name = request.POST.get('receipe_name') 
            # here last wala receipe_name hiiden wale input ka value wala hai
            
           
            r=Receipe.objects.get(receipe_name=receipe_name)
            qyt=request.POST.get('amount')
            tp=int(request.POST.get('price'))*int(qyt)
            #print(receipe_info.receipe_image)
           # receipe_info.receipe_image=os.path.basename(receipe_info.receipe_image.url)
            CartItem.objects.create(receipe_name= r,quantity=qyt,owner=request.user,price=tp)
            # here CartItem me create kr liye

      data1=CartItem.objects.filter(owner=request.user)
      tprice=0
      for d in data1:
            tprice+=d.price
      #  price = Receipe.objects.filter(price= data1[1].price)
      # print(receipe_info)
            #  print(price)
      return render(request,'cart.html',{'data':data1,"tprice":tprice})

def menuu(request):
      d=Category.objects.all()

      for i in d:
            i.receipe_image = os.path.basename(i.receipe_image.url)
      return render(request,'menu.html',{'data1':d})

def profilee(request):
      orderobj=Order.objects.filter(user=request.user)
      orders=[]
      for orobj in orderobj:
            orders.append({                       
                  'order':orobj,
                  'items':OrderItem.objects.filter(order=orobj)
            })
            # orders=OrderItem.objects.filter(order=orobj)
      return render(request,'profile.html',{"orders":orders})
      pass




# def delete(request,IDFROMURL):
#       # pass
#     try:
#        Receipe_ob = Receipe.objects.get(id= IDFROMURL)
#        Receipe_ob.delete()
#     except:
#        return render(request,'cart.html',{'Receipe':ob})

#     ob = Receipe.objects.all()
#     return render(request,'cart.html',{'Receipe':ob})
