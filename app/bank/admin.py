from django.contrib import admin
from .models import Branch, Client, Product, Account

admin.site.register(Branch)
admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Product)

