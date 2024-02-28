from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    message = models.CharField(max_length=1500)
    def __str__(self):
        return str(self.number) + ' ' + str(self.email)
