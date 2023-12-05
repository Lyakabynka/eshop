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
from core.views import *
from django.contrib.auth import views as auth_views
from core.forms import LoginForm

urlpatterns = [
    path('', landing, name='landing_page'),
    path('imprint/', imprint, name='imprint_page'),
    path('admin/', admin.site.urls),
    path('main_form_page/', forms_main, name='forms-main'),
    path('category_form/', create_category, name='create-category_page'),
    path('roles_form/', create_role, name='create-role_page'),
    path('items_form/', create_item, name='create-item_page'),
    path('discount_form/', create_discount, name='create-discount_page'),
    path('orders_form/', create_order, name='create-order_page'),
    path('delivery_data_form/', create_delivery_data, name='create-delivery-data_page'),
    path('user_item_form/', create_user_item, name='create-user-item_page'),
    path('ordered_form/', create_user_order, name='create-user-order_page'),
    path('ordered_items_form/', create_order_item, name='create-order-item_page'),
    path('owns_form/', create_owneditem_user, name='create-owneditem-user_page'),
    path('wished_user_items_form/', create_wisheditem_user, name='create-wisheditem-user_page'),
    path('successful_operation/', successful_operation, name='successful-operation_page'),
    path('items/', search_items, name='search-items_page'),
    path('items/<int:pk>/', item_detail, name='item-detail_page'),
    path('users/', search_users, name='search-users_page'),
    path('users/<int:pk>/', user_detail, name='user-detail_page'),
    path('user_wished_items/', search_wisheditems, name='search-user-wished-items_page'),
    path('user_wished_items/<int:pk>/', user_wished_items_detail, name='user-wished-items-detail_page'),
    path('orders/', search_orders, name='search-orders_page'),
    path('orders/<int:pk>/', order_detail, name='order-detail_page'),
    path('users_form/', signup, name='signup_page'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_page'),
    # autocomplete
    path('autocomplete_users/', autocomplete_users, name='autocomplete_users'),
    path('autocomplete_orders/', autocomplete_orders, name='autocomplete_orders'),
    path('autocomplete_items/', autocomplete_items, name='autocomplete_items'),
    path('map/', map, name='map_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)