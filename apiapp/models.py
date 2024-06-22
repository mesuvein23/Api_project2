from django.db import models

# Create your models here.

class ContactData(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' from ' + self.address

class Category(models.Model):
    c_name = models.CharField(max_length=100)
    c_slug = models.CharField(max_length=100)
    c_image = models.ImageField(upload_to='images/' , null=True, default="")