from django.conf import settings
from django.db import models
class Demo(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    description = models.TextField()
    amount = models.DecimalField(max_digits=30,decimal_places=10,)
    created_at = models.DateTimeField(auto_now_add=True,)
    user = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="demo_user",)

# Create your models here.
