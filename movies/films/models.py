from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from enum import Enum
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Values(Enum):
    EUR = 'Euro'
    DOL = 'Dollar'
    RUB = 'Rubles'
class Test(models.Model):

    value = [
        (Values.EUR.name, Values.EUR.value),
        (Values.DOL.name, Values.DOL.value),
        (Values.RUB.name, Values.RUB.value)
    ]

    name = models.CharField(max_length=200)
    raiting = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    author = models.CharField(max_length=30, null=True)
    is_popular = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False)
    budjet = models.IntegerField(default=0, null=True, validators=[MinValueValidator(1)])
    raiting_status = models.CharField(default='-', null=False)
    currency = models.CharField(max_length=3, choices=value, default='RUB')

    def get_url(self):
        return reverse('movie', args=[self.slug])

    def save_slug(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.raiting <= 50:
            self.raiting_status = 'OK'
        elif self.raiting<= 70:
            self.raiting_status = 'GOOD'
        else:
            self.raiting_status = 'GREAT'
        super(Test, self).save(*args, **kwargs)
    def __str__(self):
        # return "name - raiting %".format(self.name, self.raiting)
        return f"{self.name} - {self.raiting}% - {self.is_popular}"
