from django.db import models

class Contact(models.Model):
 name=models.CharField(max_length=50)
 email=models.EmailField(max_length=50)
 subject=models.CharField(max_length=50)
 message=models.TextField()

 def __str__(self):
    return self.name