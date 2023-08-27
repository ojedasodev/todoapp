from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todoItem(models.Model):
    title= models.CharField(max_length=150)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title