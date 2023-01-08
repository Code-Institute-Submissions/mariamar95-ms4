from django.test import TestCase


class TestViews(TestCase):

    """
    Test that the all_products view is rendering
    the correct template∂
    """

    def test_get_all_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
