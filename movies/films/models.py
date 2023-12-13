from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from enum import Enum
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Actors(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    ]
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актер {self.first_name} {self.last_name}"
        else:
            return f"Актриса {self.first_name} {self.last_name}"


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
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
    is_popular = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False)
    budjet = models.IntegerField(default=0, null=True, validators=[MinValueValidator(1)])
    raiting_status = models.CharField(default='-', null=False)
    currency = models.CharField(max_length=3, choices=value, default='RUB')
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, db_constraint=False)
    actors = models.ManyToManyField(Actors)

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
        # return "name - raiting %".forms(self.name, self.raiting)
        return f"{self.name} - {self.raiting}% - {self.is_popular}"
