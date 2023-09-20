from django.db import models
from django.utils.timezone import now


# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/images/products/',null=True,blank=True)

    created_at = models.DateTimeField(default=now)




    def __str__(self):
        return f'Product: {self.name} $ {self.price}'



