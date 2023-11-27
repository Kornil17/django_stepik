from django.test import TestCase
from .models import Test
from django.urls import reverse
from django.utils.text import slugify
# Create your tests here.

class TestModelTestCase(TestCase):
    @staticmethod
    def print_info(message):
        count = Test.objects.order_by('name')
        print(f"{message}: #all_movies={count}")

    def setUp(self):
        print('#' * 20)
        self.print_info('Start setUp')
        self.films = Test.objects.create(name='Legend', raiting=100, slug=slugify('Legend'))
        Test.objects.create(name='First', raiting=75, is_popular=True)
        Test.objects.create(name='Second', raiting=20, is_popular=False)
        self.print_info('End setUp')
        print('#' * 20)

    def test_create_object(self):
        """Создание запсии и проверка соответствия"""
        self.print_info('Strart test_create')
        self.assertEqual(self.films.name, 'Legend')
        self.assertEqual(self.films.raiting, 100)
        self.print_info('Finished test_create')

    def test_get_all(self):
        """Получение всех записей из БД"""
        self.print_info('Start test_get_all func')
        movies = Test.objects.all()
        self.assertEqual(len(movies), 3)
        self.print_info('Finidhed test_get_all func')
    def test_get_object(self):
        """Получение одной записи из БД"""
        self.print_info('Start test_get func')
        movies = Test.objects.get(name='Legend')
        self.assertEqual(movies.name, self.films.name)
        self.print_info('Finidhed test_get func')
    # def test_get_url(self):
    #     """Проверка метода get_url()"""
    #     self.print_info('Start test_url func')
    #     url = self.films.get_url()
    #     expected_url = reverse('movie', args=['legend'])
    #     self.assertEqual(url, expected_url)
    #     self.print_info('Finished test_url func')
    def test_get_str(self):
        """Проверка метода str"""
        self.print_info('Start test_str func')
        str = Test.objects.get(name='Legend')
        self.assertEqual(str, self.films)
        self.print_info('Finished test_str func')

    def test_get_slug(self):
        """Проверка метода slug"""
        self.print_info('Start test_slug func')
        slug = 'legend'
        self.assertEqual(slug, self.films.slug)
        self.print_info('Finished test_slug func')

    def test_get_budjet(self):
        """Проверка метода budjet"""
        self.print_info('Start test_budjet func')
        budjet = 0
        self.assertEqual(budjet, self.films.budjet)
        self.print_info('Finished test_budjet func')
    def test_delete(self):
        """Проверка удаления записи"""
        self.print_info('Start test_delete func')
        Test.objects.get(name='Legend').delete()
        self.assertEqual(0, len(Test.objects.filter(name='Legend')))
        self.print_info('Finished test_delete func')

    def test_update(self):
        """Проверка изменения данных"""
        self.print_info('Start test_update func')
        obj = Test.objects.get(name='Legend')
        obj.name = 'Lego'
        self.assertEqual('Lego', obj.name)
        self.print_info('Finished test_update func')


