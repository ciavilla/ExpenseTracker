from django.urls import path
from .views import receipt_list_view, create_receipt_view, category_list_view, account_list_view, create_category_view, create_account_view

urlpatterns = [
    path('', receipt_list_view, name='home'),
    path('create/', create_receipt_view, name='create_receipt'),
    path('categories/', category_list_view, name='category_list'),
    path('accounts/', account_list_view, name='account_list'),
    path('categories/create/', create_category_view, name='create_category'),
    path('accounts/create/', create_account_view, name='create_account'),
]
