from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  summary = models.TextField(max_length=200)
  author = models.ForeignKey(User, blank=True , on_delete=models.CASCADE)
  created_date = models.DateTimeField(auto_now_add=True)
  
  def __main__(self):
    return self.name