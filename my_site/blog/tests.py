from django.test import TestCase
from .models import Blog
from django.urls import reverse
from django.utils.text import slugify
# Create your tests here.

class BlogTestCase(TestCase):

    @staticmethod
    def print_info(message):
        return f"{message}"
    def setUp(self):
        print('#' * 20)
        self.print_info('Start set_up func')
        Blog(first_name='Maks', last_name='Kostychev', age=35, email='mk@mail.com').save()
        self.blog = Blog.objects.get(first_name='Maks')
        Blog(first_name='Dina', last_name='Osipova', age=27, email='do@mail.ru').save()
        Blog(first_name='Lana', last_name='DelaRay', age=41, email='ld@mail.com').save()
        print('#' * 20)

    def test_created(self):
        self.print_info('Start test_created func')
        name = 'Maks'
        self.assertEqual(name, self.blog.first_name)
        self.print_info('End test_created func')

        