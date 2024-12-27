from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipt, ExpenseCategory, Account
from .forms import ReceiptForm, ExpenseCategoryForm, AccountForm

# Create your views here.
def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {
        'receipts': receipts,
    }
    return render(request, 'receipts/receipt_list.html', context)


@login_required
def receipt_list_view(request):

    receipts = Receipt.objects.filter(purchaser=request.user)

    context = {
        'receipts': receipts,
    }
    return render(request, "receipts/receipt_list.html", context)


@login_required
def create_receipt_view(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)

        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect('home')
    else:
        form = ReceiptForm()

    context = {'form': form}
    return render(request, 'receipts/create_receipt.html', context)

@login_required
def category_list_view(request):
    categories = ExpenseCategory.objects.filter(owner=request.user).distinct()

    categories_with_counts = [
        {'category': category, 'receipt_count': Receipt.objects.filter(category=category, purchaser=request.user).count()}
        for category in categories
    ]

    context = {
        'categories': categories_with_counts
    }

    return render(request, 'receipts/category_list.html', context)

@login_required
def account_list_view(request):
    accounts = Account.objects.filter(owner=request.user).distinct()

    accounts_with_counts = [
        {'account': account, 'receipt_count': Receipt.objects.filter(account=account, purchaser=request.user).count()}
        for account in accounts
    ]

    context = {
        'accounts': accounts_with_counts
    }
    return render(request, 'receipts/account_list.html', context)

@login_required
def create_category_view(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()
            return redirect('category_list')
    else:
        form = ExpenseCategoryForm()

    context = {'form': form}
    return render(request, 'receipts/create_category.html', context)

@login_required
def create_account_view(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            account.save()
            return redirect('account_list')
    else:
        form = AccountForm()

    context = {'form': form}
    return render(request, "receipts/create_account.html", context)
