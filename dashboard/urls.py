from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.dashboard_index, name='dashboard_index'),
    path('add-book/', views.add_book, name='add_book'),
    path('search-book/', views.search_available_book, name='search_available_book'),
    path('view-available-books/', views.view_available_books, name='view_available_books'),
    
]