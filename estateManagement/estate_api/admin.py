from django.contrib import admin

from .models import Contact, SalesPerson

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'house', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'house')
  list_per_page = 25

class SalesPersonAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'hire_date')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25



admin.site.register(Contact, ContactAdmin)
admin.site.register(SalesPerson, SalesPersonAdmin)