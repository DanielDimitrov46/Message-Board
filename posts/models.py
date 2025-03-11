from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField(null=True, blank=True)

    def __str__(self):  # new
        return self.text[:50]