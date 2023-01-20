from django.shortcuts import redirect, render, get_object_or_404
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, CategoryForm, AccountForm

# Create your views here.
@login_required
def receipt_list(request):
  receipts = Receipt.objects.filter(purchaser=request.user)
  context = {
    "receipts": receipts,
  }
  return render(request, 'receipts/receipt_list.html', context)

@login_required
def category_list(request):
  # we want to see categories that belong to specific foreign keys
  categories = ExpenseCategory.objects.filter(owner=request.user)
  context = {
    "categories": categories,
  }
  return render(request, 'receipts/category_list.html', context)

@login_required
def account_list(request):
  accounts = Account.objects.filter(owner=request.user)
  context = {
    "accounts": accounts,
  }
  return render(request, 'receipts/account_list.html', context)

@login_required
def create_receipt(request):
  if request.method == "POST":
    print('post post post')
    form = ReceiptForm(request.POST)
    if form.is_valid():
      receipt = form.save(False)
      receipt.purchaser = request.user
      receipt.save()
      print('valid!!!!!!!!')
      return redirect('home')

  else:
    print('creating form')
    form = ReceiptForm()
  context = {
    "form" : form,
  }

  return render(request, 'receipts/receipt_create.html', context)

@login_required
def create_category(request):
  if request.method == "POST":
    form = CategoryForm(request.POST)
    if form.is_valid():
      category = form.save(False)
      category.owner = request.user
      category.save()
      return redirect('category_list')
  else:
    form = CategoryForm()
  context = {
    'form' : form,
  }
  return render(request, 'receipts/category_create.html', context)

@login_required
def create_account(request):
  if request.method == "POST":
    form = AccountForm(request.POST)
    if form.is_valid():
      account = form.save(False)
      account.owner = request.user
      account.save()
      return redirect('account_list')
  else:
    form = AccountForm()
  context = {
    'form' : form,
  }
  return render(request, 'receipts/account_create.html', context)
