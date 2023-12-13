from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.




class DressingRooms(models.Model):
    floor = models.IntegerField()
    numbers = models.IntegerField()

    def __str__(self)->str:
        return f"{self.floor}, {self.numbers}"

class Blog(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)
    dressing = models.OneToOneField(DressingRooms, on_delete=models.SET_NULL, null=True, blank=True)

    def str(self):
        return f"{self.first_name}, {self.last_name}, {self.age}"



