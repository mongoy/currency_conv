from django.test import TestCase

from conversion.models import Currency
from django.urls import reverse


class CurrencyListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 currencies for pagination tests
        number_of_currencies = 13
        for currency_num in range(number_of_currencies):
            Currency.objects.create(cur_name='C%s' % currency_num, curs=currency_num)

    def test_view_url_exists_at_desired_location(self):
        # проверка URL-адреса, просто определенный путь без указания домена
        resp = self.client.get('/currencies/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # проверка URL-адреса, генерируется из имени
        resp = self.client.get(reverse('currency-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        # проверка URL-адреса, генерируется из имени
        resp = self.client.get(reverse('currency-list'))
        self.assertEqual(resp.status_code, 200)
        # Получаем шаблон
        self.assertTemplateUsed(resp, 'conversion/currency_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('currency-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['currency_list']) == 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('currency-list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['currency-list']) == 3)
