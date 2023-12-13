from django.contrib import admin, messages
from .models import Test, Values, Author, Actors
from django.db.models import QuerySet



@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    ordering = ['id']
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    ordering = ['id']

class Raitingfilter(admin.SimpleListFilter):

    title = 'Filter by raiting'
    parameter_name = 'raiting'
    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 60', 'Средний'),
            ('от 60 до 70', 'Высокий'),
            ('>=80', 'Гуру')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(raiting__lt=40)
        if self.value() == 'от 40 до 60':
            return queryset.filter(raiting__gte=40).filter(raiting__lte=60)
        if self.value() == 'от 60 до 70':
            return queryset.filter(raiting__gte=60).filter(raiting__lte=70)
        if self.value() == '>=80':
            return queryset.filter(raiting__gte=80)
        return queryset
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    fields = ['name', 'authors']
    exclude = ['authors']
    readonly_fields = ['is_popular', 'currency', 'budjet']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['id', 'name', 'raiting', 'authors',  'is_popular', 'slug', 'budjet', 'currency', 'raiting_status']
    list_editable = ['name', 'raiting', 'authors', 'is_popular', 'slug', 'budjet', 'currency']
    ordering = ['id']
    list_per_page = 2
    filter_horizontal = ['actors']
    actions = ['set_euro', 'set_dollar', 'set_rubles']
    search_fields = ['id', 'name__istartswith', 'currency']
    list_filter = ['id', 'name', Raitingfilter]
    @admin.display(ordering='raiting', description='Отзывы')
    def raiting_status(self, test: Test) -> str:
        if test.raiting <= 50:
            return 'OK'
        if test.raiting <= 70:
            return 'GOOD'
        if test.raiting <= 80:
            return 'GREAT'
        return 'FANTASTIC'

    @admin.action(description='Set euro value')
    def set_euro(self, request, qr: QuerySet) -> None:
        count = qr.update(currency=Values.EUR.name)
        self.message_user(request, f'Вы обновили {count} записей')

    @admin.action(description='Set dollar value')
    def set_dollar(self, request, qr: QuerySet) -> None:
        count = qr.update(currency=Values.DOL.name)
        self.message_user(request, f'Вы обновили {count} записей', messages.ERROR)
    @admin.action(description='Set rubles value')
    def set_rubles(self, request, qr: QuerySet) -> None:
        count = qr.update(currency=Values.RUB.name)
        self.message_user(request, f'Вы обновили {count} записей', messages.SUCCESS)

