from django import forms
from .models import Receipt, ExpenseCategory, Account

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['vendor', 'total', 'tax', 'date', 'category', 'account']

class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'number']
