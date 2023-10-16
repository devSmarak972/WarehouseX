from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="in-store")
    quantity = models.IntegerField(default=0, null=True, blank=True)
    arrival_date = models.DateField(null=True,blank=True)
    dispatch_date = models.DateField(null=True,blank=True)
    warehouse = models.ForeignKey("Warehouse", on_delete=models.CASCADE)
    def __str__(self):
      return self.name
class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0,null=True,blank=True)
    location=models.TextField(default="Kharagpur",null=True,blank=True)
    sold=models.IntegerField(default=0,null=True,blank=True)
    sales = models.FloatField(default=0, null=True, blank=True)
    def __str__(self):
      return self.name+" "+self.location
  
class InvoiceItem(models.Model):
    name = models.CharField(max_length=255)
    product_name=models.CharField(max_length=255)
    product_qty=models.IntegerField(default=1)
    invoice=models.ForeignKey("Invoice",null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
      return self.name
class Invoice(models.Model):
    name = models.CharField(max_length=255)
    issuedby=models.CharField(max_length=255)
    issuedaddr=models.CharField(max_length=255)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    issue_date = models.DateField(null=True,blank=True)
    def __str__(self):
      return self.name