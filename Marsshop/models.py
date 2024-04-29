from django.db import models
from app.models import User

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='shop/')
    cost = models.IntegerField()
    quantitiy = models.IntegerField()

    def __str__ (self) -> str:
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    poduct = models.ForeignKey(Product, on_delete = models.CASCADE)
    quatiy = models.IntegerField()

    def __str__(self) -> str:
            return self.user.name  