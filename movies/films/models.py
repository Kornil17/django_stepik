from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=200)
    raiting = models.IntegerField()
    author = models.CharField(max_length=30, null=True)
    is_popular = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False)
    budjet = models.IntegerField(default=0, null=True)
    def get_url(self):
        return reverse('movie', args=[self.slug])

    def save_slug(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Test, self).save(*args, **kwargs)
    def __str__(self):
        # return "name - raiting %".format(self.name, self.raiting)
        return f"{self.name} - {self.raiting}% - {self.is_popular}"



