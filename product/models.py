from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/images/products/',null=True,blank=True)




    def __str__(self):
        return f'Product: {self.name} $ {self.price}'



