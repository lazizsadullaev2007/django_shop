from django.urls import path, re_path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop/', views.shop_view, name='shop'),
    path('shop/subcategories/<slug:slug>/', views.subcategory_products, name='subcategory_products'),
    path('shop/products/<slug:slug>/', views.product_detail, name='detail'),



    re_path('getSubcategory/', views.get_subcategory),

]