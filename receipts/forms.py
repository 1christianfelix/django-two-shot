from django import forms
from receipts.models import ExpenseCategory, Receipt, Account

# forms based off models
class ReceiptForm(forms.ModelForm):
  class Meta:
    model = Receipt
    fields = {
      'vendor',
      'total',
      'tax',
      'date',
      'category',
      'account',
    }
