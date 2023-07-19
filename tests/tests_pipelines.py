from django.test import TestCase
from scrapy_app.scrapy_app.pipelines import price_clean


class TestPipelines(TestCase):
    
    def test_price_clean(self):
        """
        Test that it clean price from web
        """
        data = "S/. 1,000.00"
        result = price_clean(data)
        self.assertEqual(result, '1000.00')

        data = "$ 1000.00"
        result = price_clean(data)
        self.assertEqual(result, '1000.00')

        data = "PEN 10000,00"
        result = price_clean(data)
        self.assertEqual(result, '10000.00')

