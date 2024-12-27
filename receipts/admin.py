from django.contrib import admin
from .models import ExpenseCategory, Account, Receipt

# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(Account)
admin.site.register(Receipt)
