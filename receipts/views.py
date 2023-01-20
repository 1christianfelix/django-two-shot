from django.shortcuts import redirect, render, get_object_or_404
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def receipt_list(request):
  receipts = Receipt.objects.filter(purchaser=request.user)
  context = {
    "receipts": receipts,
  }
  return render(request, 'receipts/receipt_list.html', context)
