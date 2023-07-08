from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=200)
    psw=models.CharField(max_length=8)
    cpsw=models.CharField(max_length=8)
    def __str__(self):
        return self.name
