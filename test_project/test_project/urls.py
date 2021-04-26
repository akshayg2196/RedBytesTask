
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('test_app.urls')),
    path('',include('rest_framework.urls',namespace='rest_framework')),
]
