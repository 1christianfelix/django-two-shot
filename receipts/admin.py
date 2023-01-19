from django.contrib import admin
from receipts.models import Account, ExpenseCategory, Receipt

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
  list_display = (
    "id",
    "name",
    "number",
    "owner"
  )

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
  list_display = (
    "id",
    "name",
    "owner"
  )


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
  list_display = (
    "id",
    "vendor",
    "tax",
    "date",
    "purchaser",
    "category",
    "account"
  )
