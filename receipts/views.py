from django.shortcuts import redirect, render, get_object_or_404
from receipts.models import Receipt

# Create your views here.
def receipt_list(request):
  receipts = Receipt.objects.all()
  context = {
    "receipts": receipts,
  }
  return render(request, 'receipts/receipt_list.html', context)
