from django.db import models
from django.db.models import Q

class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def availableProducts(self):
        return self.filter(product_isAvailable = True).only("product_name","product_image","product_quantity","id")
    def unavailableProducts(self):
        return self.filter(product_isAvailable = False).only("product_name","product_image","product_quantity","id")
    def quantityFilter(self,quantity,availability = False):
        return self.filter(Q(product_isAvailable = True) | Q(product_quantity__gte = quantity)).only("product_name","product_image","product_quantity","id")
    def updateQuantity(self,id,quantity):
        row = self.get(id = id)
        if row is not None:
            row.product_quantity = quantity
            row.save()
            return "Updated"
        else:
            return "Error"
class Products(models.Model):
    product_name = models.CharField(max_length=350)
    product_image = models.ImageField(max_length=200,blank = True)
    product_isAvailable = models.BooleanField(default = True)
    product_quantity = models.IntegerField(default = 0)
    product_updated = models.DateTimeField(auto_now_add = True,null = True)

    objects = ProductManager()

    def __str__(self):
        return self.product_name
    def __unicode__(self):
        return self.product_name




