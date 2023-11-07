from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='product/img')

    def __str__(self):
        self.name
class Comment(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='kament/img')

    def __str__(self):
        self.name
class Video(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='video/img')

    def __str__(self):
        self.name
class Remot(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='remot/img')

    def __str__(self):
        self.name



















