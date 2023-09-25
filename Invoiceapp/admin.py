from django.contrib import admin
from Invoiceapp.models import Invoice, InvoiceDetail
# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_dispaly=['custmore_name', 'date']
admin.site.register(Invoice, InvoiceAdmin)

class InvoiceDetailAdmin(admin.ModelAdmin):
    list_dispaly=['invoice', 'description', 'quantity', 'unit_price', 'price']
admin.site.register(InvoiceDetail, InvoiceDetailAdmin)
