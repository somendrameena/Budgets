from django.contrib import admin

from .models import ExpenseItem, ExpenseCategory, ExpenseAccount

admin.site.register(ExpenseItem)
admin.site.register(ExpenseCategory)
admin.site.register(ExpenseAccount)
