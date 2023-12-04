from django.db import models

class New(models.Model):
    title = models.CharField(max_length=45)
    net_work = models.CharField(max_length=45)
    release_date = models.DateTimeField(null=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
