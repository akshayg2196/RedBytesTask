from django.urls import path,include
from test_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.LoginView, name='login'),
    path('admin_dashboard', views.admin_Dashboard, name='admin_dashboard'),

    # Login,Logout authentication
    path('user_register', views.User_registration, name='user_register'),
    path('admin_register', views.admin_registration, name='admin_register'),

    # path('login/', auth_views.LoginView.as_view(template_name='login/login.html', authentication_form=LoginForm),
    #      name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('add_product', views.Add_Product, name='add_product'),


    # User
    path('user_dashboard', views.user_Dashboard, name='user_dashboard'),
    path('cart', views.cart, name='cart'),
    path('pluscart', views.pluscart),
    path('minuscart', views.minuscart),
    path('removecart', views.removecart),



#     API url
    path('api/', include('test_app.routers')),

#

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


