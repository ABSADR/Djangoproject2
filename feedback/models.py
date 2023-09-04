from django.db import models

# Create your models here.
class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
