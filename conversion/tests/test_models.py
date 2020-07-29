from django.test import TestCase

from conversion.models import Currency


class CurrencyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Currency.objects.create(cur_name='USD', curs=2, description='Доллар')

    def test_cur_name_label(self):
        # проверка названия колонки cur_name
        currency = Currency.objects.get(id=2)
        # Получение метаданных поля для получения необходимых значений
        field_label = currency._meta.get_field('cur_name').verbose_name
        # Сравнить значение с ожидаемым результатом
        self.assertEquals(field_label, 'Наименование валюты')

    def test_cur_name_max_length(self):
        # проверка размера колонки cur_name
        currency = Currency.objects.get(id=2)
        # Получение метаданных поля для получения необходимых значений
        max_length = currency._meta.get_field('cur_name').max_length
        # Сравнить значение с ожидаемым результатом
        self.assertEquals(max_length, 3)

    def test_object_name_is_cur_name_comma_description(self):
        currency = Currency.objects.get(id=2)
        expected_object_name = '%s, %s' % (currency.cur_name, currency.description)
        self.assertEquals(expected_object_name, str(currency))
