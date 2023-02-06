from django.db import models


class vish(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
# Create your models here.
