from django.db import models

# Create your models here.
class Invoice(models.Model):
    custmore_name=models.CharField(max_length=128)
    date=models.DateField()

    def __str__(self):
        return f"Invoice {self.id}-{self.custmore_name}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="details")
    description=models.TextField()
    quantity=models.IntegerField()
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Details for Invoice {self.invoice_id}:{self.description}"
