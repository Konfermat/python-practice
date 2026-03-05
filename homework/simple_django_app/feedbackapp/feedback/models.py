from django.db import models

# Create your models here.
class Feedback(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)