from django.db import models

# Create your models here.


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)

