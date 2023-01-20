from django.shortcuts import redirect, render, get_object_or_404
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm

# Create your views here.
@login_required
def receipt_list(request):
  receipts = Receipt.objects.filter(purchaser=request.user)
  context = {
    "receipts": receipts,
  }
  return render(request, 'receipts/receipt_list.html', context)

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
