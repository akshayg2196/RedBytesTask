from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    mobile = models.CharField(max_length=20, unique=True)
    USER_TYPE_CHOICES = (
        (1, 'vendor'),
        (2, 'user'),
    )
    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)



class admin_regModel(models.Model):
    # img = models.ImageField(upload_to='images/', null=True, blank=True)
    dob = models.DateField()
    Admin = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Admin')

    class Meta:
        db_table = "tbl_admin_reg"


class user_regModel(models.Model):

    dob = models.DateField(null=True, blank=True)
    userreg = models.OneToOneField(User, on_delete=models.CASCADE,related_name='UserData')

    class Meta:
        db_table = "tbl_user_reg"


class AddProduct(models.Model):
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)



    class Meta:
        db_table = "AddProduct"


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(AddProduct,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        return self.qty * self.product.total_amount
    class Meta:
        db_table = "Cart"
