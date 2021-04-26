from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers



from .models import *


from datetime import date


from rest_framework import serializers

from .models import *
from django.contrib.auth import authenticate


class Admin_SerializerModel(serializers.ModelSerializer):

    class Meta:
        model = admin_regModel
        fields = ["dob"]


class adminRegSerializerModel(serializers.ModelSerializer):
    Admin = Admin_SerializerModel(required=True)
    print(Admin)
    class Meta:
        model = User
        fields = ("first_name","last_name","mobile","email","password","username","role","Admin")

    def create(self, validated_data):

        print(validated_data)
        AdminData = validated_data.pop('Admin')
        print(AdminData)
        userdata = User.objects.create_user(**validated_data)
        # for i in AdminData:
            # product.categories.create(**category)
        admin_regModel.objects.create(**AdminData,Admin=userdata)
        return userdata

class User_SerializerModel(serializers.ModelSerializer):

    class Meta:
        model = user_regModel
        fields = ["dob"]


class userRegSerializerModel(serializers.ModelSerializer):
    UserData = User_SerializerModel(required=True)

    class Meta:
        model = User
        fields = ("first_name","last_name","mobile","email","password","username","role","UserData")

    def create(self, validated_data):

        print(validated_data)
        AdminData = validated_data.pop('UserData')

        user_data = User.objects.create_user(**validated_data)
        user_regModel.objects.create(**AdminData,userreg=user_data)
        return user_data



class user_reg_serilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Add_product_serializer(serializers.ModelSerializer):
    class Meta:
        model = AddProduct
        fields = "__all__"


class Cart_serializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"


    # def create(self, validated_data):
    #     print(validated_data)
    #     product = validated_data.pop('product')
    #     print(product)
        # pp=pd.to_numeric(product)
        # product_data=AddProduct.objects.get(id=pp)
        # print(product_data)
    #     user=validated_data.pop('user')
    #     user_data=User.objects.get(id=user)
    #     cart_data=Cart.objects.create(**validated_data,user=user,product=product)
    #     return product
    #


