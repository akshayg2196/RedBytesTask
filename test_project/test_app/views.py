
import datetime
from datetime import date, timedelta
from django.db.models import Max
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse
from test_app.models import *
# Create your views here.
# from e_jewelry_admin_website.models import *
from django.http import HttpResponseRedirect

from django.contrib import messages
# from e_jewelry_admin_website.serializers import *
from django.core import serializers
from .forms import SignUp
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework import serializers
# from django.contrib.auth.models import User

from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# from django.contrib.auth import login, logout
from django.contrib.auth import authenticate,login, logout
from rest_framework.decorators import api_view



class user_reg_view(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_reg_serilizer
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]



class admin_regView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = adminRegSerializerModel



class adminreg(ModelViewSet):
    queryset = admin_regModel.objects.all()
    serializer_class = Admin_SerializerModel


class user_regView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userRegSerializerModel



class userreg(ModelViewSet):
    queryset = user_regModel.objects.all()
    serializer_class = User_SerializerModel

class add_product_view(ModelViewSet):
    queryset = AddProduct.objects.all()
    serializer_class = Add_product_serializer

class cart_view(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = Cart_serializer

# Create your views here.
# def user_registration(request):
#     if request.method=="POST":
#         fm =SignUp(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm=SignUp()
#     return render(request, 'login/registration.html', {'form':fm})
context={}
def User_registration(request):

    return render(request,'login/registration.html')

def admin_registration(request):

    return render(request,'login/admin_reg.html')


def admin_Dashboard(request):

    return render(request,'base/base.html')

def user_Dashboard(request):
    context['All_product'] = AddProduct.objects.all()
    return render(request,'user/dashboard.html',context)

def LoginView(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if request.user.role==1:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            pass

    return render(request, 'login/login.html')



def Add_Product(request):

    return render(request,'AddProduct/AddProduct.html')


def cart(request):
    context = {}

    if request.user.is_authenticated:
        u = request.user
        user = User.objects.get(username=u)

        context['cart'] = Cart.objects.filter(user=user)
        amount = 0.0
        Shipping_Amount = 0.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]

        if cart_product:
            for i in cart_product:
                tempamount = i.qty * float(i.product.price)
                amount += tempamount
                total_amount = Shipping_Amount + amount
            context['amount'] = amount
            context['total_amount'] = total_amount
            return render(request, 'user/cart.html', context)
    return redirect('login')



def pluscart(request):
    if request.method == "GET":
        # u = request.session['is_logged_user']
        # context['user1'] = u
        if request.user.is_authenticated:
            u=request.user
            user = User.objects.get(username=u)
            prod_id = request.GET['prod_id']

            c = Cart.objects.get(Q(product=prod_id) & Q(user=user))

            c.qty += 1
            c.save()

            amount = 0.0
            Shipping_Amount = 0.0

            cart_product = [p for p in Cart.objects.all() if p.user == user]
            cart_count = 0
            if cart_product:
                for i in cart_product:
                    tempamount = i.qty * float(i.product.price)
                    amount += tempamount
                    cart_count+=1

        data = {'quantity': c.qty,
                        'amount': float(amount),
                        'total_amount': Shipping_Amount + amount,
                        'cart_count': cart_count
                        }
        return JsonResponse(data)


def minuscart(request):
    if request.method == "GET":
        # u = request.session['is_logged_user']
        # context['user1'] = u
        if request.user.is_authenticated:
            u=request.user
            user = User.objects.get(username=u)

            prod_id = request.GET['prod_id']

            c = Cart.objects.get(Q(product=prod_id) & Q(user=user))

            c.qty -= 1
            if c.qty > 0:
                c.save()

            amount = 0.0
            Shipping_Amount = 0.0

            cart_product = [p for p in Cart.objects.all() if p.user == user]
            cart_count=0
            if cart_product:
                for i in cart_product:
                    tempamount = float(i.qty) * float(i.product.price)
                    amount += float(tempamount)
                    cart_count += 1


        data = {'quantity': c.qty,
                    'amount': amount,
                    'total_amount': Shipping_Amount + amount,
                    'cart_count': cart_count
                    }
        return JsonResponse(data)


def removecart(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            u = request.user
            user = User.objects.get(username=u)
            prod_id = request.GET['prod_id']

            c = Cart.objects.get(Q(product=prod_id) & Q(user=user))

            c.delete()

            amount = 0.0
            Shipping_Amount = 0.0

            cart_product = [p for p in Cart.objects.all() if p.user == user]
            cart_count =0
            for i in cart_product:
                tempamount = i.qty * float(i.product.price)
                amount += tempamount
                cart_count +=1

    data = {
            'amount': amount,
            'total_amount': Shipping_Amount + amount,
            'cart_count': cart_count
        }
    return JsonResponse(data)

