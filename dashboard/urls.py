from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.dashboard_index, name='dashboard_index'),
    path('add-book/', views.add_book, name='add_book'),
    path('search-book/', views.search_available_book, name='search_available_book'),
    #path('view-available-products/', views.view_available_products, name='view_available_products'),
    #path('sell-available-products/', views.sell_available_products, name='sell_available_products'),
    #path('view-sold-products/', views.view_sold_products, name='view_sold_products'),
    #path('users/', views.users, name='users'),
]