from django.contrib import admin

from transactions.models import Tag, Transaction

admin.site.register(Tag)
admin.site.register(Transaction)
