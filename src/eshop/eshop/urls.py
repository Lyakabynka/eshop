"""
URL configuration for eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from core.views import create_user_item,create_delivery_data,create_order,create_discount,create_item,signup,landing, imprint,forms_main ,create_category, create_role

urlpatterns = [
    path('', landing, name='landing_page'),
    path('imprint/', imprint, name='imprint_page'),
    path('admin/', admin.site.urls),
    path('main_form_page/', forms_main, name='forms-main'),
    path('category_form/', create_category, name='create-category_page'),
    path('roles_form/', create_role, name='create-role_page'),
    path('users_form/', signup, name='signup_page'),
    path('items_form/', create_item, name='create-item_page'),
    path('discount_form/', create_discount, name='create-discount_page'),
    path('orders_form/', create_order, name='create-order_page'),
    path('delivery_data_form/', create_delivery_data, name='create-delivery-data_page'),
    path('user_item_form/', create_user_item, name='create-user-item_page'),
    



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)