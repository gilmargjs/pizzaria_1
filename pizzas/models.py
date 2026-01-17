from django.db import models


# Create your models here.
class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    value = models.FloatField()
    photo = models.ImageField(upload_to="pizzas/", blank=True, null=True)

    def __str__(self):  # função para retorna o nome da pizza no admin
        return self.name
